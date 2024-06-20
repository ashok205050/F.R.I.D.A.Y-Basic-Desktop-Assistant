import sys
import subprocess
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QMessageBox
from PyQt5.QtCore import QFile
from loginWindowGUI import Ui_Form
from PyQt5.QtGui import QIcon



class loginwindow(QWidget):
    def __init__(self):
        super(loginwindow, self).__init__()
        self.GUI_main = Ui_Form()
        self.GUI_main.setupUi(self)
        self.setWindowTitle('F.R.I.D.A.Y')
        self.setWindowIcon(QIcon('E:/others/others/GUI/GUIimage/logo.jpg'))
        self.GUI_main.pushButton_3.clicked.connect(self.close)


        self.GUI_main.pushButton.clicked.connect(self.ValidateLogin)
        self.GUI_main.pushButton_4.clicked.connect(self.close)
        self.GUI_main.pushButton_3.clicked.connect(self.openAnotherFile)  
        self.GUI_main.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.GUI_main.pushButton_2.clicked.connect(self.retryButton)

    def ValidateLogin(self):
        username = self.GUI_main.lineEdit.text()
        pass1 = self.GUI_main.lineEdit_2.text()
        if username == "Ashok" and pass1 == "paw":
            QMessageBox.information(self, "Login Successful", "Login Successful")
            self.runAnotherFile() 
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def retryButton(self):
        self.GUI_main.lineEdit.clear()
        self.GUI_main.lineEdit_2.clear()

    def openAnotherFile(self):
        try:
            subprocess.Popen(['python', 'E:/others/others/GUI/GUI_main/firstpagework.py'])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open another file: {str(e)}")

    def runAnotherFile(self):
        try:
            subprocess.Popen(['python', 'E:/others/others/GUI/GUI_main/mainOutput.py']) 
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to run another file: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loginwindow()
    ui.show()
    sys.exit(app.exec_())
