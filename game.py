import pygame
import sys
import draw_map
import auto
# 완성된 고리를 확인하고 싶을 때 사용
import time

# ########## DrawMap 객체를 만들고 메서드를 통해서만 해당 객체(클래스)의 변수에 접근을 함. ########## #


class Game:
    # 아래의 변수를 클래스 변수라고 함(클래스들의 전역변수 같은 느낌.)
    # apple = 0

    # 생성자 안에 변수를 인스턴스 변수라고 함.
    def __init__(self, color, width=836, height=836):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.my_color = color
        self.my_turn = True

        # 게임을 시작하게할 bool 변수.
        # 맵의 정중앙에 3 => 33, 5 => 55 둘 중 하나로 착수될 때만 본격적으로 게임이 시작될 수 있음.
        self.real_start = None
        self.system_count = 0
        self.flask_connect = None
        self.view = None

        # past x, y, 이전 좌표
        self.p_x = None
        self.p_y = None

        # ####마우스 이벤트로 사용자가 게임을 할 때#### #
        self.map = None

        # #### M C T S #### #
        self.auto = None

    # 메시지를 받는 부분.
    # def receive_message(self):

    # 게임이 직접적으로 돌아가는 루프.
    def auto_loop(self):

        self.auto = auto.Auto(self)
        self.auto.draw()

        while True:

            self.system_count += 1

            # CPU 이용률을 낮춤.
            # self.clock.tick(2)

            self.auto.auto_tile_set()

            # 흰이나 검 루프가 완성되면 맵을 초기화.
            if self.auto.is_over():
                self.auto.non_at.clear()
                self.system_count = 0
                # time.sleep(3)
                break

            # time.sleep(1)
            print(self.system_count)

    # def mouse_loop_init(self):
    #
    #     print("나의 색상은!!", self.my_color)
    #
    #     if self.my_color == "Black":
    #         self.my_turn = False
    #
    #     self.p_x = self.p_y = 9
    #     self.real_start = False
    #     self.map = draw_map.DrawMap(self)
    #     self.map.draw()

    # 게임이 직접적으로 돌아가는 루프.
    def mouse_loop(self, flask_connect, que):

        print("나의 색상은!!", self.my_color)

        self.real_start = False

        if self.my_color == "Black":
            self.my_turn = False
            self.real_start = True

        self.p_x = self.p_y = 9
        self.flask_connect = flask_connect
        self.map = draw_map.DrawMap(self)
        self.map.draw()

        while True:

            # self.system_count += 1
            # CPU 이용률을 낮춤.
            self.clock.tick(10)

            if len(que) >= 1:
                print("받은 데이터 출력", que)
                data = que.popleft()
                mes = data["tile_set"]
                mes_x = mes["X"]
                mes_y = mes["Y"]
                mes_tile = mes["Tile"]
                self.map.set_by_server(mes_x, mes_y, mes_tile)
                self.map.win_check(mes_x, mes_y)

                if self.my_color == mes["Sender"]:
                    self.my_turn = False
                    pygame.event.wait()
                else:
                    self.my_turn = True
                    pygame.event.clear()

            self.mouse_event()

            self.map.draw()

            # 승리가 판별 되면 맵을 초기화.
            if self.map.is_over():
                self.real_start = False
                self.p_x = self.p_y = 9
                self.system_count = 0
                return

            # print(self.system_count)

    # 사람 사용자가 있을 경우 사용.
    def mouse_event(self):
        events = pygame.event.get()
        for event in events:

            if not self.my_turn:
                events.clear()
                return

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and self.my_turn:

                # 현재 클릭한 좌표.
                x = event.pos[0] // 44
                y = event.pos[1] // 44

                # 최초 9, 9 좌표에 33 혹은 55 번 타일만 놓을 수 있음.
                if not self.real_start:

                    # left click, 예비 타일 3, 5번 중 하나만 놓일 수 있음.
                    if event.button == 1:
                        self.real_start, tile = self.map.first_set(1)
                        # self.map.draw()
                        # return 9, 9, tile

                    # right click, 예비 타일 3, 5번을 확정하고 게임을 본격적으로 시작함.
                    elif event.button == 3:
                        self.real_start, tile = self.map.first_set(3)
                        self.flask_connect.tile_set_request(self.my_color, 9, 9, tile)
                        # self.map.draw()
                        # return 9, 9, tile

                # 본격적인 게임 시작
                else:

                    # 현재 좌표와 이전 좌표가 같은지 확인.
                    if not (x == self.p_x and y == self.p_y):

                        # 예비 타일을 저장한 리스트를 초기화, 추천 타일을 찾음, 카운트 초기화.
                        self.map.find_recommend_tiles(x, y)

                    # 확정된 타일이 아닐경우
                    if not self.map.is_set(x, y):  # if_is_not_set

                        # left click, 좌클릭한 경우
                        if event.button == 1:

                            # 예비 타일을 놓아줌.
                            self.map.tile_choose(x, y, self.p_x, self.p_y)

                        # right click, 우클릭한 경우.
                        elif event.button == 3:

                            # 타일 확정, 착수, 자동완성!!
                            tile = self.map.tile_set(self.p_x, self.p_y)

                            if tile > 10:
                                self.flask_connect.tile_set_request(self.my_color, self.p_x, self.p_y, tile)

                            # self.map.win_check(self.p_x, self.p_y)
                            # self.map.draw()
                            # return self.p_x, self.p_y, tile

                    # 현재 타일의 좌표를 저장
                    self.p_x = x
                    self.p_y = y

        # self.map.draw()
        # return -1, -1, -1
