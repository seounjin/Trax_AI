from View import form
from SocketIo import server_connect
from SocketIo.connector import Connector
from SocketIo.battle import Battle
import time
from Game.game import Game


class Controller:
    def __init__(self):
        self.view = form.Form()

        self.connector = None
        self.view.room_index = None

        # 버튼
        self.view.room_listWidget.itemDoubleClicked.connect(self.room_doubleclick)
        self.view.btn_renew.clicked.connect(self.renew_click)
        self.view.room_ready.clicked.connect(self.ready_click)
        self.view.btn_exit.clicked.connect(self.exit_click)
        self.view.join_btn.clicked.connect(self.join_click)
        self.view.check_btn.clicked.connect(self.check_click)
        self.view.btn_Ai.clicked.connect(self.ai_vs)
        self.view.login_btn.clicked.connect(self.login_click)

        # self.view.login_btn.clicked.connect(lambda s=None, i=1: self.set_stack_index(s, i))
        self.view.btn_Battle.clicked.connect(lambda s=1, i=2: self.set_stack_index(s, i))
        self.view.room_out.clicked.connect(lambda s=2, i=2: self.set_stack_index(s, i))
        self.view.sign_btn.clicked.connect(lambda s=0, i=4: self.set_stack_index(s, i))
        self.view.exit_btn.clicked.connect(lambda s=None, i=0: self.set_stack_index(s, i))
        # self.view.room_listWidget.itemDoubleClicked.connect(lambda s=None, i=3: self.set_stack_index(s, i))

        # id check
        self.check_id = False
        self.check_pass = False
        self.check_name = False
        self.check_email = False

    def ai_vs(self):
        # ##### Man Vs AI ##### #
        color = "White"  # 항상 White 가 선공!!
        game = Game(color, "AI", 836, 836)
        game.ai_loop()
        return

    def room_doubleclick(self, item):  # 방 번호 더블 클릭 이벤트
        self.view.room_index = self.view.room_listWidget.row(item)
        self.view.room_index_id["user_id"] = self.view.user_id
        self.view.room_index_id["room_index"] = self.view.room_index
        self.view.flask_connect.join_room(self.view.room_index_id)

        time.sleep(1)
        if self.view.flask_connect.room == True:
            self.set_stack_index(0, 3)

    def renew_click(self):
        print("갱신버튼 클릭")
        self.view.flask_connect.room_request()

    def set_stack_index(self, s, index):
        self.view.st_layout.setCurrentIndex(index)

        # if index == 1:  # 로그인 버튼
        #     #server_connect.login()
        #     self.view.user_id = self.view.login_In.text()
        #     server_connect.login_request(self.view.user_id)

        if index == 2 and s == 1:  # 1:1 버튼
            self.connector = Connector()
            self.view.flask_connect = self.connector.register_namespace(Battle('/battle', self.view))
            self.view.flask_connect.room_request()

        elif index == 2 and s == 2:  # 방나가는 버튼
            print("방 나가기 버튼")
            self.view.flask_connect.leave_room(self.view.room_index_id)
            self.view.flask_connect.room_request()

    def ready_click(self):
        print("레디버튼 클릭")
        # self.view.id_left.setText(whit_black["white"])
        # self.view.id_right.setText(whit_black["black"])

        if self.view.id_left.text() == self.view.user_id+'님':  # white 일 때
            self.view.flask_connect.ready_request({"ready": {"room_index": self.view.room_index, "color": "white"}})  # 방번호,black,white
        else:
            self.view.flask_connect.ready_request({"ready": {"room_index": self.view.room_index, "color": "black"}})  # 방번호,black,white

    def exit_click(self):
        server_connect.exit_request(self.view.user_id)
        self.connector.disconnect()
        server_connect.login_disconnect()
        print("종료")
        exit()

    def join_click(self):

        if len(self.view.password.text()) != 0 and len(self.view.password2.text()) != 0:
            if self.view.password.text() == self.view.password2.text():
                self.check_pass = True
                self.view.password_check.setText("비밀번호가 일치합니다")
            else:
                self.view.password_check.setText("비밀번호가 일치하지 않습니다")

        if len(self.view.name.text()) != 0:
            self.check_name = True

        if len(self.view.email.text()) != 0:
            self.check_email = True

        if self.check_id == True and self.check_pass == True and self.check_name == True and self.check_email == True:

            # id,password,name,email
            u_id = self.view.id.text()
            u_password = self.view.password.text()
            u_name = self.view.name.text()
            u_email = self.view.email.text()

            user_info = {"join": {"id": u_id,
                                  "password": u_password,
                                  "name": u_name,
                                  "email": u_email,
                                  }}

            server_connect.join_request(user_info)

            time.sleep(1)
            if server_connect.join_check == True:
                self.view.id.setText("")
                self.view.password.setText("")
                self.view.password2.setText("")
                self.view.name.setText("")
                self.view.email.setText("")

                self.view.password_check.setText("")
                self.view.id_check.setText("ID 중복검사를 해주십쇼")

                self.view.msg_set("회원가입이 완료 되었습니다")
                self.set_stack_index(0, 0)

                server_connect.join_check = False
                self.check_id = False
                self.check_pass = False
                self.check_name = False
                self.check_email = False

        else:
            self.view.msg_set("다시한번 확인해주시기 바랍니다")

    def check_click(self):
        u_id = self.view.id.text()
        server_connect.id_check(u_id)

        time.sleep(1)
        if server_connect.client_id_check == True:
            self.view.id_check.setText("사용할 수 있는 ID 입니다")
            self.check_id = True
        else:
            self.view.id_check.setText("사용할 수 없는 ID 입니다")

    def login_click(self):
        self.view.user_id = self.view.login_In.text()
        json = {'id': self.view.user_id, 'password': self.view.passward_In.text()}
        server_connect.login_request(json)

        time.sleep(1)
        if server_connect.login_check == 1:
            self.set_stack_index(0, 1)
        elif server_connect.login_check == 0:
            self.view.msg_set("ID와 password를 다시 확인해주시기 바랍니다")
        else:
            self.view.msg_set("현재 ID가 접속중입니다")





