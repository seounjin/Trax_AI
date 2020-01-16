import pygame as pg
import sys
import map
import auto as att

import MCTS as mcts

class Game():

    def __init__(self, width=1600, height=1600):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.map = map.DrawMap(self)
        self.at = att.Auto()

        self.mt = mcts.Tree_Node()
        #self.ex_mov = None


    def main_loop(self):

        root = self.mt.make_root() # 루트노느 생성
        current = root

        while True:
            self.handle_events()
            self.map_draw()

            if self.map.init_t:
                self.map.init_tile(self.map.init_t)
                current.backup(1)  # 겜 끝나면 백업
                continue

            current = current.select_leaf()  # 리프 검사

            a,b,tile_at = self.at.auto_set_tile()  # 자동으로 착수 타일 리턴값 x,y,tile



            #current.leaf.expand(1)  # 확장 한번만 되게 해야함

            self.map.auto_complete(a, b)  # 자동완성기능


            break


    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT: sys.exit()

            elif event.type == pg.MOUSEBUTTONUP:
                x = event.pos[0] // 44
                y = event.pos[1] // 44
                print("마우스 좌표", x, y,map.mapArray[x][y])
                # 확정된 타일이 아닐경우
                if map.mapArray[x,y] != 11 and map.mapArray[x,y] != 22 and map.mapArray[x,y] != 33 and map.mapArray[x,y] != 44 and map.mapArray[x,y] != 55 and map.mapArray[x,y] != 66:
                    if event.button == 1:  # left click
                        #self.map.tile_chose(x, y)
                        a,b = self.at.auto_set_tile()  # 처음 넣고
                        self.map.auto_complete(a, b)  # 자동완성


                    elif event.button == 3 and map.mapArray[x,y] != 0:  # right click
                        self.map.tile_Select(x, y)
                        self.map.auto_complete(x, y)  # 자동완성

    def map_draw(self):
        self.map.draw()
        pg.display.flip()














