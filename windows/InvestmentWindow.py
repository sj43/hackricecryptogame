import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QFile, QObject


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        btn = self.window.findChild(QPushButton, 'back_button')
        btn.clicked.connect(self.ok_handler)
        self.window.show()

    def ok_handler(self):
        print('works!')


app = QApplication(sys.argv)
form = Form('investment_window.ui')
sys.exit(app.exec_())
