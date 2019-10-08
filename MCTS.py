import collections
import numpy as np
import math


class UCTNode():
    def __init__(self,move, parent=None):
        self.move = move
        self.is_expanded = False
        self.parent = parent  # Optional[UCTNode]
        self.children = {}  # Dict[move, UCTNode]
        self.child_priors = np.zeros([362], dtype=np.float32)
        self.child_total_value = np.zeros([362], dtype=np.float32)
        self.child_number_visits = np.zeros([362], dtype=np.float32)


    # 1단계
    def child_Q(self):
        return self.child_total_value / (1 + self.child_number_visits)

    def child_U(self):
        return math.sqrt(self.number_visits) * (self.child_priors / (1 + self.child_number_visits))

    def best_child(self):
        return np.argmax(self.child_Q() + self.child_U())

    def select_leaf(self):
        current = self
        while current.is_expanded:
            best_move = current.best_child()
            current = current.maybe_add_child(best_move)
        return current


    # 2단계
    def expand(self, child_priors):
        self.is_expanded = True
        self.child_priors = child_priors

    def maybe_add_child(self, move):
        if move not in self.children:
            self.children[move] = UCTNode(move, parent=self)
        return self.children[move]

    # 3단계
    def backup(self, value_estimate: float):
        current = self
        while current.parent is not None:
            current.number_visits += 1
            current.total_value += (value_estimate *
                                    self.game_state.to_play)
            current = current.parent
















