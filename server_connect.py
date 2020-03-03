import socketio

sio = socketio.Client()
#sio = socketio.Client(logger=True, engineio_logger=True)

def login():
    sio.connect('http://192.168.200.175:5000')
    #sio.connect('http://172.16.2.186:5000')
    # sio.connect('http://127.0.0.1:5000/')

@sio.event
def login_request(data):  # 로그인 요청
    sio.emit('login', data)  # emit(이벤트, json)

@sio.event
def exit_request(data):  # 종료
    sio.emit('exit', data)  # emit(이벤트, json)

@sio.on('login')
def on_message(data):  # 들어온 메세지 확인
    print(data + '님이 로그인 되심')



def login_disconnect():
    sio.disconnect()

# class Server_connect():
#     def __init__(self):
#         #self.sio = socketio.Client(logger=True, engineio_logger=True)
#         self.sio = socketio.Client()
#         self.sio.connect('http://127.0.0.1:5000')
#
#     def login_request(self,data):  # 로그인 요청
#         self.sio.emit('login', data)  # emit(이벤트, json)
#
#     def on_message(self,data):  # 들어온 메세지 확인
#         print(data + '님이 로그인 되심')