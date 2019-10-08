import game

'''
pg.init()

#screen = pg.display.set_mode((400,400))

draw_map = map.DrawMap()
#draw_map.draw()

draw_map.draw()

while True:
    for event in pg.event.get():

        if event.type == pg.MOUSEBUTTONUP:
            #pos = pg.mouse.get_pos()
            x = event.pos[0]//44
            y = event.pos[1]//44

            print(map.mapArray(x,y))
            #map.mapArray(x,y)

            print(event.pos,x,y)



        if event.type == pg.QUIT:
            pg.QUIT()
            sys.exit()
        pg.display.update()

'''

# if __name__ == "__main__": 의 조건문 뒤의 코드는, 해당 조건문이 있는 파일에서만 실행되고, 다른 파일에 import 했을 시 실행되지 않는다.
if __name__ == "__main__":
    game = game.Game()
    game.main_loop()










