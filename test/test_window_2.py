import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QListWidget, QMainWindow, QWidget
from PySide2.QtCore import QFile, QObject, Signal, Slot

class MainWindow(QObject):

    open_bank = Signal()
    open_crypto = Signal()
    open_property = Signal()
    open_investment = Signal()

    living_expenses = Signal(int)
    card_repay = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        app = QApplication(sys.argv)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.window.show()
        sys.exit(app.exec_())




class PropertyWindow(QMainWindow):

    buy_property = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(PropertyWindow, self).__init__(parent)







"""
app = QApplication(sys.argv)
window = QUiLoader().load("property_window.ui")
window.show()
sys.exit(app.exec_())
"""


MainWindow("main_window.ui")

