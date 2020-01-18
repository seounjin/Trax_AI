from connector import SocketNamespace


class Battle(SocketNamespace):
    def __init__(self, namespace, view):
        super(Battle, self).__init__(namespace)  # 부모
        self.namespace = namespace
        self.view = view

    def ready_request(self, data):
        self.emit('battle', data)  # 방번호,레디 유무

    def room_request(self):  # 방 리스트 요청
        self.emit('battle', "room_list")  # emit(이벤트, json)

    def join_room(self, data):  # 메세지 보내기
        self.emit('join', data)  # emit(이벤트, json)

    def leave_room(self, data):  # 방에서 나가기
        self.emit('leave', data)  # emit(이벤트, json)

    def on_message(self, data):  # 들어온 메세지 확인
        self.view_update(data)

    def on_connect(self):  # 연결
        print('1:1 연결함요')

    def on_disconnect(self):
        print('서버 연결 끊어짐요')

    def view_update(self, data):

        if "room_Info" in data:
            for num in range(3):
                if not len(data["room_Info"][str(num)]):  # 방이 비어 있을 경우
                    self.view.room_listWidget.item(num).setText("빈방")
                elif len(data["room_Info"][str(num)]) == 2:  # 2명
                    self.view.room_listWidget.item(num).setText(
                        data["room_Info"][str(num)][0] + " vs " + data["room_Info"][str(num)][1])
                else:  # 1명
                    self.view.room_listWidget.item(num).setText(data["room_Info"][str(num)][0])

        elif "white_black" in data:
            whit_black = data["white_black"]  # 방접속 유저
            self.view.id_left.setText(whit_black["white"])
            self.view.id_right.setText(whit_black["black"])

        elif "ready" in data:
            print(data["ready"])

        elif data == "gamestart":
            print("겜시작")
