import imp
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface3 import Ui_MainWindow
from function import Function_UI
import serial, serial.tools.list_ports
import time
class MainWindow():
    def __init__(self):
        n=100
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.serial = Function_UI()
        self.serialPort = serial.Serial()
        
   


        self.uic.baund_list.addItems(self.serial.baudList)
        self.uic.baund_list.setCurrentText('9600')
        self.update_ports()
        self.uic.Connect_Button.clicked.connect(self.connect_serial)
        self.uic.Send_Button.clicked.connect(self.send_data)
        self.uic.Clear_Button.clicked.connect(self.clear)
        self.uic.Update_Button.clicked.connect(self.update_ports)
        self.serial.data_available.connect(self.update_view)
        
        
        self.uic.progressBar.setMinimum(0)
        self.uic.progressBar.setMaximum(1024)
    def update_view(self,data):
        self.uic.textBrowser.append(data)
        self.uic.progressBar.setValue(int(data))

    def connect_serial(self):
        if(self.uic.Connect_Button.isChecked()):
            port = self.uic.port_list.currentText()
            baud = self.uic.baund_list.currentText()
            self.serial.serialPort.port = port
            self.serial.serialPort.baudrate = baud
            self.serial.connect_serial()
            if(self.serial.serialPort.is_open):
                self.uic.Connect_Button.setText("Disconnect")
        else:
            self.serial.disconnect_serial()
            self.uic.Connect_Button.setText("Connect")
    

    def send_data(self):
        data_send = self.uic.Send_text.toPlainText()
        self.serial.send_data(data_send)

    def update_ports(self):
        self.serial.update_port()
        self.uic.port_list.clear()
        self.uic.port_list.addItems(self.serial.portList)

    def clear(self):
        self.uic.textBrowser.clear()

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())