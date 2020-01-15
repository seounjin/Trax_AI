import numpy as np
import pygame as pg
from collections import deque
import sys
import time

# 2816
# 타일수
# 한 타일당 44픽셀
map_x = 64
map_y = 64

tile_dict = {0: pg.image.load('tile/0.png'),
             1: pg.image.load('tile/1_tmp.png'),
             2: pg.image.load('tile/2_tmp.png'),
             3: pg.image.load('tile/3_tmp.png'),
             4: pg.image.load('tile/4_tmp.png'),
             5: pg.image.load('tile/5_tmp.png'),
             6: pg.image.load('tile/6_tmp.png'),

             11: pg.image.load('tile/1.png'),
             22: pg.image.load('tile/2.png'),
             33: pg.image.load('tile/3.png'),
             44: pg.image.load('tile/4.png'),
             55: pg.image.load('tile/5.png'),
             66: pg.image.load('tile/6.png')
             }

tile_info = {  # 위 ,오른쪽,아래쪽,왼쪽
    11: ["B", "W", "W", "B"],
    22: ["B", "B", "W", "W"],
    33: ["W", "B", "B", "W"],
    44: ["W", "W", "B", "B"],
    55: ["W", "B", "W", "B"],
    66: ["B", "W", "B", "W"]
}

# 위 오른쪽 아래 왼쪽
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

arr_reverse = [2, 3, 0, 1]

mapArray = np.zeros((map_x, map_y))

sys.setrecursionlimit(10000)  # 재귀 제한 풀기


class DrawMap:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.countMouseClick = 0
        self.white_x = 0
        self.white_y = 0
        self.init_t = False

    def init_tile(self,init_t):
        if init_t:
            mapArray.fill((0))
            self.init_t=False
            #time.sleep(5)

    def draw(self):
        for x in range(0, map_x):
            for y in range(0, map_y):
                current_tile = tile_dict[mapArray[x, y]]
                self.screen.blit(current_tile, (x * 44, y * 44))

    def tile_chose(self, x, y):

        self.countMouseClick += 1

        mapArray[x][y] = self.countMouseClick % 7

    def tile_Select(self, x, y):

        mapArray[x][y] = (self.countMouseClick % 7) * 10 + self.countMouseClick % 7

    # def white_win(self, x, y, white_info, color, check=False):
    #
    #     direct_w = 0
    #
    #     if mapArray[x][y] == 0:
    #         return
    #
    #     if (x == self.white_x and y == self.white_y) and (check == True and color == 'W'):
    #         # print("하얀색이김")
    #         print("하얀색이김", x, y)
    #         # pg.quit()
    #         # sys.exit()
    #         return
    #
    #     if (x == self.white_x and y == self.white_y) and (check == True and color == 'B'):
    #         print("검은색이김", x, y)
    #         # print(x,y)
    #         # pg.quit()
    #         # sys.exit()
    #         return
    #
    #     if check is False:  # 착수한타일 방향 넘겨주고
    #         direct_w = white_info
    #         check = True
    #     else:
    #         tile_n = mapArray[x][y]  # 현재 위치한 타일
    #         for i in range(4):
    #             if tile_info[tile_n][i] == color and arr_reverse[white_info] != i:
    #                 direct_w = i
    #                 break
    #
    #     if direct_w == 0:
    #         self.white_win(x, y - 1, direct_w, color, check)
    #     elif direct_w == 1:
    #         self.white_win(x + 1, y, direct_w, color, check)
    #     elif direct_w == 2:
    #         self.white_win(x, y + 1, direct_w, color, check)
    #     elif direct_w == 3:
    #         self.white_win(x - 1, y, direct_w, color, check)

    def rfindroof(self, mX, mY, toin, color):

        tile = mapArray[mX][mY]

        if color == 'W':
            print("현재 탐색 좌표", mX, mY)
            print("되돌아가야 하는 좌표",self.white_x, self.white_y)

        temp = toin

        if tile == 0:
            #print("고리 미완성 탈출~~~~~~~~~~~~~~~~~~~~")
            return

        if mX == self.white_x and mY == self.white_y:
            print(color, "고리 완성 탈출!!!!!!!!!!!!!!!!!!!!!!!")
            self.init_t=True
            
            sys.exit()
            return

        for i in range(4):
            if i != toin and tile_info[tile][i] == color:
                out = i
                break

        if out == 0:
            mY = mY - 1
            temp = 2

        elif out == 1:
            mX = mX + 1
            temp = 3

        elif out == 2:
            mY = mY + 1
            temp = 0

        elif out == 3:
            mX = mX - 1
            temp = 1

        self.rfindroof(mX, mY, temp, color)


    def findroof(self, X, Y, color):

        x = X

        y = Y

        tile = mapArray[X][Y]

        if tile == 0:  # 승리햇을시에 그다음 한번더 블랙 타일 재귀가 되므로 초기화 되었을때 타일 좌표를 0을 반환 할수 있으므로 리턴조건
            return

        print(x, y, color, "고리 탐색 시작")
        #print(tile,"번 타일부터 탐색")
        #print(self.white_x, self.white_y)

        firstin = 0

        for i in range(4):
            if tile_info[tile][i] == color:
                firstin = i
                break

        if firstin == 0:
            firstin = 2;
            y = y - 1

        elif firstin == 1:
            firstin = 3
            x = x + 1

        elif firstin == 2:
            firstin = 0
            y = y + 1

        elif firstin == 3:
            firstin = 1
            x = x - 1

        self.rfindroof(x, y, firstin, color)
        #time.sleep(5)

    def auto_complete(self, x, y):
        if x == -5 and y == -5: #처음 착수할시 리턴종료
            return

        if x == -1 and y == -1:
            return

        que = deque()
        que2 = deque()
        green_x, green_y = 0, 0  # 초록색타일 위치값

        for i in range(4):  # 착수한 타일의 기준으로 주변 초록색 타일 검사
            ex, ey = x + dx[i], y + dy[i]  # 위 오른쪽 아래 왼쪽
            if mapArray[ex][ey] == 0:
                que.append([ex, ey])

        while que:  # 초록색 타일 기준으로 주변 타일 카운트
            # print("제일위")
            cnt = 0
            green_x, green_y = que.popleft()  # 초록색 타일 좌표
            for i in range(4):
                ex, ey = green_x + dx[i], green_y + dy[i]
                if mapArray[ex][ey] != 0:
                    cnt += 1
                    que2.append([ex, ey, arr_reverse[i]])  # 방향위치 정보값

            if cnt == 0:
                continue
            if cnt <= 1:
                que2.popleft()
                continue

            col = ['0'] * 4  # 초록색 타일에 들어갈 타일 색깔 정보
            color_info = 0

            while que2:  # 초록색 타일에 원하는 타일 값 넣는 반복문
                t_x, t_y, loc = que2.popleft()
                tile_n = mapArray[t_x][t_y]
                col[arr_reverse[loc]] = tile_info[tile_n][loc]
                color_info = arr_reverse[loc]

            real_num = 4 - col.count('0')
            fcnt = 0
            tile_t = 0

            for i in tile_info:
                cnt = 0
                for j in range(4):
                    if tile_info[i][j] != col[j]:
                        continue
                    else:  # 뽑아낸 색깔 같을때 카운트
                        cnt += 1

                if real_num == cnt:
                    fcnt += 1
                    tile_t = i

            if fcnt == 1:  # 카운트 수가 같다면 해당위치 착수
                mapArray[green_x][green_y] = tile_t
                self.white_x = green_x
                self.white_y = green_y
                self.findroof(green_x, green_y, 'W')
                self.findroof(green_x, green_y, 'B')
                # self.white_win(green_x, green_y, color_info, 'W', False)
                # self.white_win(green_x, green_y, color_info, 'B', False)
                self.auto_complete(green_x, green_y)

