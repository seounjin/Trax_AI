from PySide2.QtWidgets import *
from controller import Controller

if __name__ == '__main__':
    app = QApplication([])
    Controller()
    app.exec_()
