from random import *
import draw_map


# For M.C.T.S Data
class Auto(draw_map.DrawMap):

    # self.adjacent_tiles 은 큐임.
    def __init__(self, game):

        draw_map.DrawMap.__init__(self, game)

        # nonSet_adjacent_tiles
        # 착수되지 않은(초록색) 위, 오른, 아래, 왼쪽 인접 좌표를 담는 리스트.
        self.non_at = ([])

    def enqueue_adjacent_tile(self, x, y):

        # 위 오른쪽 아래 왼쪽, 순서로 인접 타일의 좌표를 넣음.
        if y - 1 >= 0:
            if draw_map.mapArray[x, y - 1] == 0:
                self.non_at.append([x, y - 1])

        if x + 1 <= 18:
            if draw_map.mapArray[x + 1, y] == 0:
                self.non_at.append([x + 1, y])

        if y + 1 <= 18:
            if draw_map.mapArray[x, y + 1] == 0:
                self.non_at.append([x, y + 1])

        if x - 1 >= 0:
            if draw_map.mapArray[x - 1, y] == 0:
                self.non_at.append([x - 1, y])

        self.non_at = list(set(map(tuple, self.non_at)))

        # 중복 제거. ==> unhashable type: 'list'
        # 리스트는 사전의 키로 사용 불가능.
        # self.non_at = list(set(self.non_at))
        # self.non_at = list(set([tuple(set(item)) for item in self.non_at]))
        # print(self.non_at)

    # auto tile set
    def auto_tile_set(self):

        self.draw()

        # 최초 타일 놓기.
        if draw_map.mapArray[9, 9] == 0:

            # 클릭카운트에 0과 1 중에 랜덤으로 선택된 수 대입.
            # 바로 접근하지 않고 대입할 수 있는 방법 찾기!!
            self.click_count = randint(0, 1)

            # draw_map class 의 멤버 함수인 first_set 의 elif 에 걸리기 위한 임시조취.
            draw_map.mapArray[9, 9] = 7
            self.first_set(3)

            self.enqueue_adjacent_tile(9, 9)
            return

        # 착수 되지 않은 인접 타일의 리스트의 인덱스 하나를 랜덤으로 뽑음.
        # 중복을 제거하고 사용할 수 있는 x, y를 뽑아주는 메서드가 있으면 좋을 것 같음.
        end = len(self.non_at) - 1
        index = randint(0, end)
        x = self.non_at[index][0]
        y = self.non_at[index][1]
        self.non_at.pop(index)

        self.enqueue_adjacent_tile(x, y)

        # self.find_adjacent_tiles(x, y)
        self.find_recommend_tiles(x, y)
        end2 = len(self.adjacent_tiles) - 1

        if end2 == -1:
            return

        print("          end Of index + 1 ", end2 + 1, "개     ", self.adjacent_tiles)
        index2 = randint(0, end2)
        self.p_tile = self.adjacent_tiles[index2]
        draw_map.mapArray[x, y] = 7
        self.tile_set(x, y)

        self.draw()
