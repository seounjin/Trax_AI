import socketio

sio = socketio.Client()
#sio = socketio.Client(logger=True, engineio_logger=True)

client_id_check = None
join_check = False

def sio_connect():
    sio.connect('http://127.0.0.1:5000')

@sio.event
def login_request(data):  # 로그인 요청
    sio.emit('login', data)  # emit(이벤트, json)

@sio.event
def id_check(data):  # id 중복체크 요청
    sio.emit('check', data)  # emit(이벤트, id)

@sio.event
def join_request(data):  # 회원가입 요청
    sio.emit('join', data)  # emit(이벤트, json)

@sio.event
def exit_request(data):  # 종료
    sio.emit('exit', data)  # emit(이벤트, json)

@sio.on('login')
def login_message(data):
    print(data + '님이 로그인 되심')

@sio.on('client_id_check')
def id_check_message(data):
    global client_id_check

    if data == 'T':
        client_id_check = True
    else:
        client_id_check = False

@sio.on('join_check')
def join_message(data):
    global join_check

    if data == 'T':
        join_check = True


def login_disconnect():
    sio.disconnect()

