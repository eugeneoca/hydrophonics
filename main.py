import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from dashboard import Ui_MainWindow


class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.uiDefinitions()

        # Updates
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_ui)
        self.timer.start()


    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        
    def update_ui(self):
        print("Updating")
        # Update Date & Time
        time_now = datetime.now()
        current_datetime = str(time_now.strftime("%B %d, %Y - %H:%M:%S"))
        self.txt_date.setText(current_datetime)

if __name__ == '__main__':
    print("Hydrophonics Software V1.0")
    time_now = datetime.now()
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()