import collections
import numpy as np
import math

class DummyNode(object):

  def __init__(self):
    self.parent = None
    self.child_total_value = collections.defaultdict(float)
    self.child_number_visits = collections.defaultdict(float)


class MCTSNode():

    def __init__(self, move,leaf_x,leaf_y,leaf_tile,parent=None):
        if parent is None:
            parent = DummyNode()
        self.move = move
        self.is_expanded = False
        self.parent = parent  # Optional[UCTNode]
        self.children = {}  # Dict[move, UCTNode]
        self.child_priors = np.zeros((10, 10), dtype=np.float32)
        self.child_total_value = np.zeros((10, 10), dtype=np.float32)
        self.child_number_visits = np.zeros((10, 10), dtype=np.float32)

        self.leaf_x = leaf_x
        self.leaf_y = leaf_y
        self.leaf_tile = leaf_tile
        self.children2 = collections.defaultdict(MCTSNode)

    # 1단계
    def child_Q(self):
        return self.child_total_value / (1 + self.child_number_visits)

    def child_U(self):
        return math.sqrt(self.number_visits) * (self.child_priors / (1 + self.child_number_visits))

    def best_child(self):
        return np.argmax(self.child_Q() + self.child_U())

    def select_leaf(self):
        current = self

        while current.is_expanded: #여기서 선택하는건가
            best_move = current.best_child()

            current = current.maybe_add_child(best_move)

        return current


    # 2단계
    def expand(self, child_priors): #노드생서된거
        self.is_expanded = True
        self.child_priors = child_priors


    def maybe_add_child(self, move):
        if move not in self.children:
            self.children[move] = MCTSNode(move, parent=self) # 노드 추가
        return self.children[move]

    # 3단계
    def backup(self, value_estimate: float):
        current = self
        while current.parent is not None:
            current.number_visits += 1
            current.total_value += (value_estimate * 1)
            current = current.parent


    # def find_leaf(self, x, y, tile):  # 리프찾기
    #
    #     if len(self.children) == 0: # 루트노드만 있을 경우
    #         return self
    #
    #     for i in range(12):
    #         if self.children2[i].
    #
    #     # for i in self.children:
    #     #     if i.leaf_x == x and i.leaf_y and i.leaf_tile:
    #     #         return i
    #
    #     return self





class NeuralNet():
  @classmethod
  def evaluate(self, game_state):
    return np.random.random([362]), np.random.random() # 362개 배열안에 0.0 에서 1.0 사이 임의의 부동소수점 반환

# def UCT_search(mct):
#     #mct = MCTSNode()
#
#     leaf = mct.parent.select_leaf()
#     child_priors, value_estimate = NeuralNet.evaluate(leaf.game_state)
#     leaf.expand(child_priors)
#     #leaf.backup(value_estimate)


class Tree_Node():
    # def __init__(self):
    #     self.mct = MCTSNode(1, 0, 0, 0, parent=None) # 루트노드 생성


    def make_root(self): # 루트노드 생성
          self.mct = MCTSNode(1,0,0,0,parent=None)
          return self.mct



    # def first_node(self,mct):
    #     leaf = mct.parent.select_leaf()
    #     child_priors, value_estimate = NeuralNet.evaluate(leaf.game_state)
    #
    #
    # def find_leaf(self, x, y, tile):  # 리프찾기
    #     # self.leaf_x = x
    #     # self.leaf_y = y
    #     # self.leaf_tile = tile
    #     if len(self.mct.children) == 0: # 루트노드만 있을 경우
    #         return self
    #
    #     for i in self.mct.children:
    #         if i.leaf_x == x and i.leaf_y and i.leaf_tile:
    #             self.find_leaf(x, y, tile)










