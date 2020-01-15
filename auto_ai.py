import random
from collections import deque
import map as mp



class Auto:
    def __init__(self,adjacent_tiles =deque()):
        self.adjacent_tiles = adjacent_tiles

    def enque_adjacent_tile(self,x,y):

        # 위 오른쪽 아래 왼쪽
        if mp.mapArray[x][y-1] == 0:
            self.adjacent_tiles.append([x, y-1])
        if mp.mapArray[x+1][y] == 0:
            self.adjacent_tiles.append([x+1, y])
        if mp.mapArray[x][y+1] == 0:
            self.adjacent_tiles.append([x, y+1])
        if mp.mapArray[x-1][y] == 0:
            self.adjacent_tiles.append([x-1, y])

    def auto_set_tile(self):

        # 처음으로 타일 착수하는 조건문
        if mp.mapArray[10][10] == 0: # 처음 타일 착수할 자리
            first_t = [33, 55]
            ran = random.sample(first_t, 1)
            mp.mapArray[10][10] = ran[0]
            self.enque_adjacent_tile(10,10)

            return -5,-5,ran[0]

        # 큐값에서 초록색타일이 아닌 좌표 값제거 반복문
        # print(self.adjacent_tiles)
        # for i in self.adjacent_tiles:
        #     if mp.mapArray[i[0]][i[1]] !=0:
        #         self.adjacent_tiles.remove([i[0], i[1]])

        # 랜덤으로 인접한 좌표값 뽑아내기
        ran = random.sample(self.adjacent_tiles, 1)
        t_x,t_y = ran[0][0],ran[0][1]

        if mp.mapArray[t_x][t_y] !=0:
            self.adjacent_tiles.remove([t_x, t_y])
            return -1,-1,0

        # 뽑아낸 큐에서 값 제거
        self.adjacent_tiles.remove([t_x,t_y])

        # 위 오른쪽 아래 왼쪽
        t_color={} # key:방향 ,value:색깔
        # 랜덤으로 뽑아낸 좌표값의 인접타일 색깔찾기
        if mp.mapArray[t_x][t_y-1] != 0: # 타일 위일 경우 아래 색깔
            r_t=mp.mapArray[t_x][t_y-1]
            t_color[0] = mp.tile_info[r_t][2]

        if mp.mapArray[t_x+1][t_y] != 0:  # 타일 오른쪽일 경우 아래 색깔
            r_t = mp.mapArray[t_x+1][t_y]
            t_color[1] = mp.tile_info[r_t][3]

        if mp.mapArray[t_x][t_y+1] != 0:  # 타일 아래일 경우 아래 색깔
            r_t = mp.mapArray[t_x][t_y+1]
            t_color[2] = mp.tile_info[r_t][0]

        if mp.mapArray[t_x-1][t_y] != 0:  # 타일 왼쪽일 경우 아래 색깔
            r_t = mp.mapArray[t_x-1][t_y]
            t_color[3] = mp.tile_info[r_t][1]

        # 랜덤으로 뽑을 타일 리스트
        r_tile = []
        # key:방향 ,value:색깔
        # 찾은 색깔 타일 찾기
        t_color_len=len(t_color)
        for i in mp.tile_info:
            cnt = 0
            for j in t_color:
                if t_color[j] == mp.tile_info[i][j]:
                    cnt += 1

            # 인접타일 1개일 때와 2개일때 조건문
            if t_color_len == 1 and cnt == 1:
                r_tile.append(i)
            elif t_color_len == 2 and cnt == 2:
                r_tile.append(i)

        if len(r_tile)==0:
            #print("0일때",t_x,t_y)
            return -1,-1 ,0

        #print("색깔",r_tile)
        ran2 = random.sample(r_tile, 1)
        mp.mapArray[t_x][t_y] = ran2[0]
        self.enque_adjacent_tile(t_x,t_y)


        return t_x,t_y , ran2[0]


















