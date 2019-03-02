# main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

if __name__ == "__main__":
    app = QApplication(sys.argv)

    file = QFile("mainwindow.ui")
    file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(file)
    window.show()

    sys.exit(app.exec_())