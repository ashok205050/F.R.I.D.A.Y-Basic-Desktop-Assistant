import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
import main  

class AssistantThread(QThread):
    text_updated = pyqtSignal(str)
    user_input = pyqtSignal(str) 

    def __init__(self, text_edit, schedule_text_edit, parent=None):
        super().__init__(parent)
        self.text_edit = text_edit
        self.schedule_text_edit = schedule_text_edit

    def run(self):
        assistant = main.Assistant()
        assistant.text_output.connect(self.display_text)
        self.user_input.connect(assistant.user_input) 
        assistant.run_assistant()

    def display_text(self, text):
        self.text_edit.append(text)

    def receive_user_input(self, user_input):
        self.schedule_text_edit.setText(user_input)

class MainWindow(QWidget):
    user_input = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('F.R.I.D.A.Y')  
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.start_button = QPushButton('Start Assistant', self)
        self.start_button.clicked.connect(self.start_assistant)
        layout.addWidget(self.start_button)

        self.schedule_text_edit = QTextEdit(self)
        layout.addWidget(self.schedule_text_edit)

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

        self.assistant_thread = AssistantThread(self.text_edit, self.schedule_text_edit)
        self.user_input.connect(self.get_user_input)

    def start_assistant(self):
        self.start_button.setEnabled(False)
        self.assistant_thread.start()

    def get_user_input(self):
        user_input = self.schedule_text_edit.toPlainText()
        self.assistant_thread.receive_user_input(user_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
