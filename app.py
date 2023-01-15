import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI import Ui_Dialog
import Login, Help415, AddFriead
from threading import Thread
from ThreadCustom import ThreadWithReturnValue
import time



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_Dialog()
        self.uic.setupUi(self)

        self.thread = {}
        self.uic.spinThread.setSpecialValueText(str(10))
        self.uic.spinDelay.setSpecialValueText(str(5))
        self.table = self.uic.twListAcc
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(2, 50)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 100)
        
        self.uic.pbSelectFile.clicked.connect(self.browserFiles)
        self.uic.pbImport.clicked.connect(self.importAccounts)
        self.uic.pbSend.clicked.connect(self.start_worker_1)
        self.uic.pbAddFriead.clicked.connect(self.start_worker_2)

    def start_worker_1(self):
        self.uic.tabWidget.setCurrentIndex(0)
        table = self.table
        txtContent = self.uic.txtContents
        self.thread[0] = Worker_1(self)
        self.thread[0].start()
        self.thread[0].signal.connect(self.login_progress)
    
    def start_worker_2(self):
        if self.uic.leUserFB.text() == '':
            self.msg('Vui lòng nhập acc chính!')
            return
        self.uic.tabWidget.setCurrentIndex(0)
        table = self.table
        txtContent = self.uic.txtContents
        self.thread[1] = Worker_2(self)
        self.thread[1].start()
        self.thread[1].signal.connect(self.login_progress)
        
    def getStatusProgress(self, num):
        switcher = {
            1:'Đang đăng nhập',
            2:'Checking 2FA',
            3:'Giải mãi 2FA..',
            4:'Pass thiết bị lạ ...',
            5:'Giải mãi 2FA...',
            6:'Đăng nhập thành công',
            7:'Err7: Đăng nhập thất bại',
            8: 'Facebook help 415',
            9: 'Cover captcha to base64',
            10: 'Đang bypass captcha',
            11: 'Retry Bypass captcha',
            12: 'Hoàn thành',
            13: 'Err13: Lỗi',
            14: 'Sai tài khoản hoặc mật khẩu',
            15: 'Không có tài khoản Need hoặc Die',
            16: 'Đang kết bạn',
            17: ' Kết bạn thành công',
            18: 'Không thể kết bạn',
            19: 'Đã kết bạn từ trước'
        }
        return switcher.get(num, 'Err: Status login')
    def login_progress(self, dict):
        if not dict:
            return
        stt = dict['stt']
        num = dict['progress']
        if num ==404:
           self.msg('Không có dữ liệu')
           return
        self.uic.pbSend.setEnabled(False)
        if num ==200:
            self.uic.pbSend.setEnabled(True)
            return
        progress = self.getStatusProgress(num)
        root = self.table.invisibleRootItem()
        obj = root.child(stt)
        if '2fa' in dict:
            obj.setText(4, dict['2fa'])      
        obj.setText(4, progress)

    def browserFiles(self):
        fileName = QFileDialog.getOpenFileName(None, "Select file", '', 'Text files (*.txt)' )
        self.uic.lePath.setText(fileName[0])
    def importAccounts(self):
        self.table.clear()
        _translate = QCoreApplication.translate
        path = self.uic.lePath.text()
        #try:
        with open(path, 'r') as f:
            count=0
            for line in f:
                cell = line.strip().split('|')
                if len(cell) > 2:
                    rowCount = self.table.topLevelItemCount()
                    self.table.addTopLevelItem(QTreeWidgetItem(rowCount))
                    self.table.topLevelItem(count).setText(0, _translate("Dialog", str(count+1)))
                    self.table.topLevelItem(count).setText(1, _translate("Dialog", cell[0]))
                    self.table.topLevelItem(count).setText(2, _translate("Dialog", cell[1]))
                    self.table.topLevelItem(count).setText(3, _translate("Dialog", cell[2]))
                    count+=1
        #except:
            #msg = self.msg("sảy ra lỗi khi import file")

    def msg(self, text):
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('icon/icon-diaglog.png'))
            msg.setIcon(QMessageBox.Critical)
            msg.setText(text)
            msg.setWindowTitle("Error")
            msg.exec_()
class Worker_2(QThread):
    signal = pyqtSignal(dict)
    def __init__(work, self):
        super().__init__()
        work.table = self.table
        work.txtContent = self.uic.txtContents
        work.thread_count = self.uic.spinThread.value()
        work.user_id = self.uic.leUserFB.text()
    def run(work):
        root = work.table.invisibleRootItem()
        child_count = root.childCount()
        if child_count<1:
            work.signal.emit({'stt': 0, 'progress': 404})
            return
        thread_value = work.thread_count
        temple_child_count = child_count
        r=0
        thread_list=[]
        thread_list_2 = []
        while(temple_child_count>0):
            if temple_child_count < thread_value:
                thread_value = temple_child_count
            r2 = r
            r3 = r
            for n in range(0,thread_value):
                obj = root.child(r)
                user_id = obj.text(1)
                password = obj.text(2)
                code2fa = obj.text(3)
                thread = ThreadWithReturnValue(target=Login.start, args=(work, r, user_id, password, code2fa))
                thread_list.append(thread)
                thread_list[r].start()
                r+=1
            for n in range(0,thread_value):
                session = thread_list[r2].join()
                thread = ThreadWithReturnValue(target=AddFriead.main, args=(work, r2, session))
                thread_list_2.append(thread)
                if session != 'ERR':
                    thread_list_2[r2].start()
                r2+=1
            #for n in range(0,thread_value):
            #    thread_list_2[r3].join()
            #    r3+=1
            temple_child_count-=thread_value
        work.signal.emit({'stt': r, 'progress': 200})

    def stop(work):
        print('Stopping thread...')
        work.terminate()

class Worker_1(QThread):
    signal = pyqtSignal(dict)
    def __init__(work, self):
        super().__init__()
        work.table = self.table
        work.txtContent = self.uic.txtContents
        work.thread_count = self.uic.spinThread.value()
    def run(work):
        root = work.table.invisibleRootItem()
        child_count = root.childCount()
        if child_count<1:
            work.signal.emit({'stt': 0, 'progress': 404})
            return
        thread_value = work.thread_count
        temple_child_count = child_count
        r=0
        thread_list=[]
        thread_list_2 = []
        while(temple_child_count>0):
            if temple_child_count < thread_value:
                thread_value = temple_child_count
            r2 = r
            r3 = r
            for n in range(0,thread_value):
                obj = root.child(r)
                user_id = obj.text(1)
                password = obj.text(2)
                code2fa = obj.text(3)
                thread = ThreadWithReturnValue(target=Login.start, args=(work, r, user_id, password, code2fa))
                thread_list.append(thread)
                thread_list[r].start()
                r+=1
            for n in range(0,thread_value):
                session = thread_list[r2].join()
                thread = ThreadWithReturnValue(target=Help415.main, args=(work, r2, session))
                thread_list_2.append(thread)
                thread_list_2[r2].start()
                r2+=1
            for n in range(0,thread_value):
                thread_list_2[r3].join()
                r3+=1
            temple_child_count-=thread_value
        work.signal.emit({'stt': r, 'progress': 200})

    def stop(work):
        print('Stopping thread...')
        work.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())