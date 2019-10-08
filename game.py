import pygame as pg
import sys
import map
import auto_ai as att
import  time


class Game():

    def __init__(self, width=1600, height=1600):
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.map = map.DrawMap(self)
        self.at = att.Auto()

    def main_loop(self):
        while True:
            self.handle_events()
            self.map_draw()

            if self.map.init_t:
                self.map.init_tile(self.map.init_t)
                continue

            a,b = self.at.auto_set_tile()  # 자동으로 착수 타일
            #time.sleep(0.1)
            self.map.auto_complete(a, b)  # 자동완성기능


            #time.sleep()

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














