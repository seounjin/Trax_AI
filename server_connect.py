import socketio

sio = socketio.Client()
#sio = socketio.Client(logger=True, engineio_logger=True)


def login():
    sio.connect('http://127.0.0.1:5000')


@sio.event
def login_request(data):  # 로그인 요청
    sio.emit('login', data)  # emit(이벤트, json)


@sio.on('login')
def on_message(data):  # 들어온 메세지 확인
    print(data + '님이 로그인 되심')

