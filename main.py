import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from dashboard import Ui_MainWindow


class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.uiDefinitions()

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()


if __name__ == '__main__':
    print("Hydrophonics Software V1.0")
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()