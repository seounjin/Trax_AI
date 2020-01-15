import socketio


class Connector:
    def __init__(self):
        #self.url = url #  나중에 url 추가
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        self.sio.connect('http://127.0.0.1:5000', namespaces=['/battle'])

    def register_namespace(self, namespaceSocket):
        self.sio.register_namespace(namespaceSocket)
        return self.sio.namespace_handlers[namespaceSocket.namespace]

    def connect(self):  # 나중에 사용
        pass


class SocketNamespace(socketio.ClientNamespace):
    def __init__(self, namespace):
        super(SocketNamespace,self).__init__()
        self.r_data = {}
        self.namespace = namespace

