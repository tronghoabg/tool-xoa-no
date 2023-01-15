# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon-diaglog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 71, 20))
        self.label_3.setObjectName("label_3")
        self.spinDelay = QtWidgets.QSpinBox(Dialog)
        self.spinDelay.setGeometry(QtCore.QRect(220, 10, 51, 20))
        self.spinDelay.setMaximum(5)
        self.spinDelay.setProperty("value", 5)
        self.spinDelay.setObjectName("spinDelay")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 41, 16))
        self.label_4.setObjectName("label_4")
        self.spinThread = QtWidgets.QSpinBox(Dialog)
        self.spinThread.setGeometry(QtCore.QRect(100, 10, 51, 20))
        self.spinThread.setMinimum(1)
        self.spinThread.setMaximum(20)
        self.spinThread.setProperty("value", 20)
        self.spinThread.setObjectName("spinThread")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 591, 501))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.pbSelectFile = QtWidgets.QPushButton(self.tab_1)
        self.pbSelectFile.setGeometry(QtCore.QRect(380, 20, 31, 23))
        self.pbSelectFile.setObjectName("pbSelectFile")
        self.lePath = QtWidgets.QLineEdit(self.tab_1)
        self.lePath.setGeometry(QtCore.QRect(40, 20, 321, 20))
        self.lePath.setObjectName("lePath")
        self.pbImport = QtWidgets.QPushButton(self.tab_1)
        self.pbImport.setGeometry(QtCore.QRect(430, 20, 101, 23))
        self.pbImport.setObjectName("pbImport")
        self.twListAcc = QtWidgets.QTreeWidget(self.tab_1)
        self.twListAcc.setGeometry(QtCore.QRect(10, 70, 551, 391))
        self.twListAcc.setObjectName("twListAcc")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 130, 251, 171))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.leUserFB = QtWidgets.QLineEdit(self.groupBox)
        self.leUserFB.setGeometry(QtCore.QRect(20, 60, 171, 20))
        self.leUserFB.setText("")
        self.leUserFB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.leUserFB.setObjectName("leUserFB")
        self.pbAddFriead = QtWidgets.QPushButton(self.groupBox)
        self.pbAddFriead.setGeometry(QtCore.QRect(150, 130, 61, 21))
        self.pbAddFriead.setObjectName("pbAddFriead")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 130, 261, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label.setObjectName("label")
        self.pbSend = QtWidgets.QPushButton(self.groupBox_3)
        self.pbSend.setGeometry(QtCore.QRect(140, 140, 75, 21))
        self.pbSend.setObjectName("pbSend")
        self.txtContents = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.txtContents.setGeometry(QtCore.QRect(30, 50, 201, 81))
        self.txtContents.setObjectName("txtContents")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Venus Tool++"))
        self.label_3.setText(_translate("Dialog", "Luồng chạy"))
        self.label_4.setText(_translate("Dialog", "Delay"))
        self.pbSelectFile.setText(_translate("Dialog", "..."))
        self.lePath.setText(_translate("Dialog", "C:\\Users\\trong\\Desktop\\acc.txt"))
        self.pbImport.setText(_translate("Dialog", "Nhập Acc"))
        self.twListAcc.headerItem().setText(0, _translate("Dialog", "#"))
        self.twListAcc.headerItem().setText(1, _translate("Dialog", "UID"))
        self.twListAcc.headerItem().setText(2, _translate("Dialog", "PASS"))
        self.twListAcc.headerItem().setText(3, _translate("Dialog", "2FA"))
        self.twListAcc.headerItem().setText(4, _translate("Dialog", "STATUS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "MAIN"))
        self.groupBox.setTitle(_translate("Dialog", "Kết bạn"))
        self.pbAddFriead.setText(_translate("Dialog", "Kết Bạn"))
        self.label_5.setText(_translate("Dialog", "Id user facebook"))
        self.groupBox_3.setTitle(_translate("Dialog", "Spam Link 415"))
        self.label.setText(_translate("Dialog", "Nội dung"))
        self.pbSend.setText(_translate("Dialog", "Bắt Đầu"))
        self.txtContents.setPlainText(_translate("Dialog", "You traveled within the last 60 days"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "CONTROLS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
