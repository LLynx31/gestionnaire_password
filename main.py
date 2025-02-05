from PySide6.QtWidgets import QMainWindow, QApplication
from Main_ui import Ui_MainWindow

if __name__ == "__main__" :
    app = QApplication([])
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    app.exec()