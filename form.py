from PySide2.QtWidgets import *


class Form(QWidget):

    def __init__(self):
        super(Form, self).__init__()  # 상위 클래스 생성자 호출, 돌려받을 객체의 타입을 지정, 폼타입으로 큐위젯객체를 생성

        # socketio
        self.flask_connect = None
        self.room_index = None

        # id
        self.user_id = ""
        self.room_index_id = {}

        # 위젯 생성
        self.wgt_login = QWidget()
        self.wgt_select = QWidget()
        self.wgt_room = QWidget()
        self.wgt_room_list = QWidget()
        self.room_listWidget = QListWidget()
        self.signup_widget = QWidget()

        self.login_screen()
        self.select_screen()
        self.list_screen()
        self.room_screen()
        self.join_screen()
        self.stack_add()
        self.show()

    def login_screen(self):
        # 위젯객체 생성
        # self.wgt_Login = QWidget()

        # 레이아웃 생성
        self.vb = QVBoxLayout()
        self.hbTop = QHBoxLayout()
        self.hbMid = QHBoxLayout()
        self.hbBot = QHBoxLayout()

        # V박스 레이아웃에 H박스 3개 추가 (V는 세로 ,H는 가로)
        self.vb.addLayout(self.hbTop)
        self.vb.addLayout(self.hbMid)
        self.vb.addStretch()
        self.vb.addLayout(self.hbBot)

        self.wgt_login.setLayout(self.vb)

        # 라벨
        self.lbl_Id = QLabel("ID: ")
        self.lbl_Ps = QLabel("PASSWORD: ")

        # 텍스트에디터
        self.login_In = QLineEdit()
        self.passward_In = QLineEdit()

        # 버튼
        self.btn_1 = QPushButton("LOGIN")
        self.btn_2 = QPushButton("SING UP")

        # 레이아웃에 ID 추가
        self.hbTop.addWidget(self.lbl_Id)
        self.hbTop.addWidget(self.login_In)

        # 레이아웃에 페스워드
        self.hbMid.addWidget(self.lbl_Ps)
        self.hbMid.addWidget(self.passward_In)

        # 레이아웃에 버튼 추가
        self.hbBot.addWidget(self.btn_1)
        self.hbBot.addWidget(self.btn_2)

    def select_screen(self):
        # 레이아웃 생성
        self.select_vb = QVBoxLayout()

        # 버튼
        self.btn_Battle = QPushButton("1 Vs 1")
        self.btn_Ai = QPushButton("User Vs AI")

        # 레이아웃에 버튼 추가
        self.select_vb.addWidget(self.btn_Battle)
        self.select_vb.addWidget(self.btn_Ai)

        # 위젯에 vb 레이아웃 추가
        self.wgt_select.setLayout(self.select_vb)

    def list_screen(self):
        # self.listWidget.setAlternateColors(True)

        # 레이아웃
        self.list_top_vb = QVBoxLayout()
        self.list_bottom_vb = QVBoxLayout()
        self.list_mainLayout = QVBoxLayout()
        self.btn_renew = QPushButton("renew")
        self.btn_exit = QPushButton("exit")

        self.list_top_vb.addWidget(self.room_listWidget)
        self.list_bottom_vb.addWidget(self.btn_renew)
        self.list_bottom_vb.addWidget(self.btn_exit)

        self.list_mainLayout.addLayout(self.list_top_vb)
        self.list_mainLayout.addLayout(self.list_bottom_vb)

        self.wgt_room_list.setLayout(self.list_mainLayout)

        # 방 초기화
        for num in range(3):
            self.room_listWidget.insertItem(num, "빈 방")

    def room_screen(self):
        # 레이아웃 생성
        self.room_vb = QVBoxLayout()
        self.room_hTop = QHBoxLayout()
        self.room_hMid = QHBoxLayout()
        self.room_hBot = QHBoxLayout()

        # V박스 레이아웃에 H박스 3개 추가 (V는 세로 ,H는 가로)
        self.room_vb.addLayout(self.room_hTop)
        self.room_vb.addLayout(self.room_hMid)
        self.room_vb.addLayout(self.room_hBot)

        self.wgt_room.setLayout(self.room_vb)

        # 라벨
        self.room_white = QLabel("White")
        self.room_black = QLabel("Black")
        self.id_left = QLabel("None")
        self.id_right = QLabel("None")

        # 버튼
        self.room_ready = QPushButton("ready")
        self.room_out = QPushButton("exit")

        # white,black 라벨 레이아웃에 추가
        self.room_hTop.addWidget(self.room_white)
        self.room_hTop.addWidget(self.room_black)

        # 방에 들어온 ID 라벨 레이아웃에 추가
        self.room_hMid.addWidget(self.id_left)
        self.room_hMid.addWidget(self.id_right)

        # 레디,exit 레이아웃에 추가
        self.room_hBot.addWidget(self.room_ready)
        self.room_hBot.addWidget(self.room_out)

    def join_screen(self):
        self.join_form = QFormLayout()
        self.setLayout(self.join_form)

        self.box_id = QHBoxLayout()
        self.id = QLineEdit()
        self.check_btn = QPushButton("check")
        self.box_id.addWidget(self.id)
        self.box_id.addWidget(self.check_btn)
        self.join_form.addRow("ID: ", self.box_id)

        self.id_check = QLabel("ID 중복검사를 해주십쇼")
        self.join_form.addWidget(self.id_check)

        self.password = QLineEdit()
        self.join_form.addRow("password: ", self.password)
        self.password2 = QLineEdit()
        self.join_form.addRow("한번더: ", self.password2)
        self.password_check = QLabel(" ")
        self.join_form.addWidget(self.password_check)

        self.name = QLineEdit()
        self.join_form.addRow("name: ", self.name)

        self.email = QLineEdit()
        self.join_form.addRow("email: ", self.email)

        self.box_btn = QHBoxLayout()
        self.join_btn = QPushButton("join")
        self.exit_btn = QPushButton("exit")
        self.box_btn.addWidget(self.join_btn)
        self.box_btn.addWidget(self.exit_btn)
        self.join_form.addRow(self.box_btn)
        self.signup_widget.setLayout(self.join_form)

    def stack_add(self):
        self.st_layout = QStackedLayout()
        self.st_layout.addWidget(self.wgt_login)
        self.st_layout.addWidget(self.wgt_select)
        # self.st_layout.addWidget(self.room_listWidget)
        self.st_layout.addWidget(self.wgt_room_list)
        self.st_layout.addWidget(self.wgt_room)
        self.st_layout.addWidget(self.signup_widget)

        self.setLayout(self.st_layout)

    def msg_set(self,content):
        # 메세지 박스
        msgBox = QMessageBox()
        msgBox.setText(content)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
