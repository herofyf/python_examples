import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "a.ui" # Enter file here.

mydialog, QtBaseClass = uic.loadUiType(qtCreatorFile)



class MyApp(QtGui.QDialog):
    def __init__(self, parent = None):
        #super(MyApp, self).__init__(parent)
        QtGui.QDialog.__init__(self)
        QtGui.QWidget.__init__(self, parent)

        self.ui = mydialog()
        self.ui.setupUi(self)
        self.ui.calc_tax_button.clicked.connect(self.CalculateTax)


    def CalculateTax(self):
        self.ui.textval.setText("fuck you")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())