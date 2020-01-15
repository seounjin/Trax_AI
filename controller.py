import form
import server_connect
from connector import Connector
from battle import Battle


class Controller:
    def __init__(self):
         self.view = form.Form()

         # socketio
         self.flask_connect = None

         self.room_index = None

         # 버튼
         self.view.room_listWidget.itemDoubleClicked.connect(self.room_doubleclick)
         self.view.btn_renew.clicked.connect(self.renew_click)
         self.view.room_ready.clicked.connect(self.ready_click)

         self.view.btn_1.clicked.connect(lambda s=None, i=1: self.set_stack_index(s, i))
         self.view.btn_Battle.clicked.connect(lambda s=1, i=2: self.set_stack_index(s, i))
         self.view.room_listWidget.itemDoubleClicked.connect(lambda s=None, i=3: self.set_stack_index(s, i))
         self.view.room_out.clicked.connect(lambda s=2, i=2: self.set_stack_index(s, i))

    def room_doubleclick(self, item):  # 방 번호 더블 클릭 이벤트
        self.room_index = self.view.room_listWidget.row(item)
        self.view.room_index_id["user_id"] = self.user_id
        self.view.room_index_id["room_index"] = self.room_index
        self.flask_connect.join_room(self.view.room_index_id)

    def renew_click(self):
        print("갱신버튼 클릭")
        self.flask_connect.room_request()

    def set_stack_index(self, s, index):
        self.view.st_layout.setCurrentIndex(index)

        if index == 1:  # 로그인 버튼
            server_connect.login()
            self.user_id = self.view.login_In.text()
            server_connect.login_request(self.user_id)

        elif index == 2 and s == 1:  # 1:1 버튼
            self.connector = Connector()
            self.flask_connect = self.connector.register_namespace(Battle('/battle', self.view))
            self.flask_connect.room_request()

        elif index == 2 and s == 2:  # exit 버튼
            print("나가기 버튼")
            self.flask_connect.leave_room(self.view.room_index_id)
            self.flask_connect.room_request()

    def ready_click(self):
        print("레디버튼 클릭")
        # self.view.id_left.setText(whit_black["white"])
        # self.view.id_right.setText(whit_black["black"])

        if self.view.id_left.text() == self.user_id+'님':  # white 일 때
            self.flask_connect.ready_request({"ready": {"room_index": self.room_index, "color": "white"}})  # 방번호,black,white
        else:
            self.flask_connect.ready_request({"ready": {"room_index": self.room_index, "color": "black"}})  # 방번호,black,white
