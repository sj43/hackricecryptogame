import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QListWidget
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
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.window.show()


MainWindow('main_window.ui')