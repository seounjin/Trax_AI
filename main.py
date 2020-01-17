import game

# if __name__ == "__main__": 의 조건문 뒤의 코드는, 해당 조건문이 있는 파일에서만 실행되고, 다른 파일에 import 했을 시 실행되지 않는다.
if __name__ == "__main__":
    game = game.Game()
    game.main_loop()
