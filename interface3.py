# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 771, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setGeometry(QtCore.QRect(10, 160, 271, 81))
        self.Clear_Button.setObjectName("Clear_Button")
        self.Send_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Send_Button.setGeometry(QtCore.QRect(10, 250, 191, 71))
        self.Send_Button.setObjectName("Send_Button")
        self.Send_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Send_text.setGeometry(QtCore.QRect(210, 250, 421, 71))
        self.Send_text.setObjectName("Send_text")
        self.Connect_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_Button.setGeometry(QtCore.QRect(10, 340, 181, 61))
        self.Connect_Button.setObjectName("Connect_Button")
        ####################
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Connect_Button.setFont(font)
        self.Connect_Button.setStyleSheet("#connect_Button:checked{\n" #yesil buton
"background-color: rgb(0, 255, 127);\n"
"}")
        self.Connect_Button.setCheckable(True)
        self.Connect_Button.setObjectName("connect_Button")
        ###########################################
        self.baund_list = QtWidgets.QComboBox(self.centralwidget)
        self.baund_list.setGeometry(QtCore.QRect(200, 350, 201, 51))
        self.baund_list.setObjectName("baund_list")
        self.Update_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Update_Button.setGeometry(QtCore.QRect(410, 340, 181, 61))
        self.Update_Button.setObjectName("Update_Button")
        self.port_list = QtWidgets.QComboBox(self.centralwidget)
        self.port_list.setGeometry(QtCore.QRect(600, 350, 181, 51))
        self.port_list.setObjectName("port_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 330, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 330, 55, 16))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 470, 691, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.oku_buton = QtWidgets.QPushButton(self.centralwidget)
        self.oku_buton.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.oku_buton.setObjectName("oku_buton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Clear_Button.setText(_translate("MainWindow", "clear"))
        self.Send_Button.setText(_translate("MainWindow", "send"))
        self.Connect_Button.setText(_translate("MainWindow", "connect"))
        self.Update_Button.setText(_translate("MainWindow", "update"))
        self.label.setText(_translate("MainWindow", "baund"))
        self.label_2.setText(_translate("MainWindow", "port"))
        self.oku_buton.setText(_translate("MainWindow", "deger oku"))
