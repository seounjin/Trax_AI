from PySide2.QtWidgets import *
from controller import Controller
import server_connect


if __name__ == '__main__':
    app = QApplication([])
    Controller()
    #server_connect.sio_connect()
    app.exec_()
