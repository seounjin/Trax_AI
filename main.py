from PySide2.QtWidgets import *
from View.controller import Controller
from SocketIo import server_connect

if __name__ == '__main__':
    app = QApplication()
    Controller()
    server_connect.sio_connect()
    app.exec_()
