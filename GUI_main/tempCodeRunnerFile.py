import sys
import subprocess
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QIcon
from firstpage import Ui_GUI_main

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        self.GUI_main = Ui_GUI_main()
        self.GUI_main.setupUi(self)
        self.setWindowTitle('F.R.I.D.A.Y')
        self.setWindowIcon(QIcon('E:/others/others/GUI/GUIimage/logo.jpg'))


        self.GUI_main.pushButton_3.clicked.connect(self.close)
        self.GUI_main.pushButton_2.clicked.connect(self.openLoginWindow)

    def openLoginWindow(self):
        # Open loginWindowwork.py in a subprocess
        try:
            subprocess.Popen(['python', 'E:/others/others/GUI/GUI_main/loginWindowwork.py'])
        except Exception as e:
            print(f"Failed to open loginWindowwork.py: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())
