import sys
from PyQt5 import QtWidgets, uic

form_class = uic.loadUiType('C:\GitHub\Coding\Emily\guidesign\FirstGuiYipeesarcastic.ui')

class MyFirstWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
myWindow = MyFirstWindow()
myWindow.show()
app.exec_()