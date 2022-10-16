import sys
sys.path.append("..")

from Model.PuzzleBoard import PuzzleBoard
from typing import List


class BoardServices(object):

    __current_puzzle: PuzzleBoard = None
    __zero_index: int = 0
    __puzzle_state = []
    __puzzle_depth: int = 0

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BoardServices, cls).__new__(cls)
        return cls.instance

    def set_board_dim(self, length: int, width: int):
        self.__length = length
        self.__width = width
        self.__goal_state = [i for i in range(self.__length * self.__width)]

    def __swap(self, i, j):
        new_state = self.__puzzle_state.copy()
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def __up(self):
        if self.__zero_index > self.__length:
            return PuzzleBoard(self.__swap(self.__zero_index, self.__zero_index - self.__length), self.__current_puzzle, 'Up', self.__puzzle_depth + 1)
        return None

    def __down(self):
        if self.__zero_index < self.__length * (self.__width - 1):
            return PuzzleBoard(self.__swap(self.__zero_index, self.__zero_index + self.__length), self.__current_puzzle, 'Down', self.__puzzle_depth + 1)
        return None

    def __left(self):
        if self.__zero_index % self.__length != 0:
            return PuzzleBoard(self.__swap(self.__zero_index, self.__zero_index - 1), self.__current_puzzle, 'Left', self.__puzzle_depth + 1)
        return None

    def __right(self):
        if (self.__zero_index + 1) % self.__length != 0:
            return PuzzleBoard(self.__swap(self.__zero_index, self.__zero_index + 1), self.__current_puzzle, 'Right', self.__puzzle_depth + 1)
        return None

    def get_children(self, puzzle_board: PuzzleBoard):
        self.__current_puzzle = puzzle_board
        self.__puzzle_state = [x for x in puzzle_board.get_state()]
        self.__zero_index = self.__puzzle_state.index(0)
        self.__puzzle_depth = puzzle_board.get_depth()
        children = [self.__up(), self.__down(), self.__left(), self.__right()]
        return list(filter(None, children))

    def is_goal(self, state: List[int]):
        if self.__length * self.__width == len(state):
            # print(self.__length + self.__width)
            for i, x in enumerate(state):
                if x != self.__goal_state[i]:
                    return False
            return True
        return False

    def manhattan_h(self, state: List[int]):
        if self.__length + self.__width == len(state):
            total = 0
            for i, x in enumerate(state):
                total += abs(i % self.__length - x % self.__length) + abs(i // self.__width - x // self.__width)
            return total
        return -1

    def euclidean_h(self, state: List[int]):
        if self.__length + self.__width == len(state):
            total = 0
            for i, x in enumerate(state):
                total += (i % self.__length - x % self.__length)**2 + abs(i // self.__width - x // self.__width)**2
            return total
        return -1


# singleton = BoardServices()
# new_singleton = BoardServices()
# singleton.l = 4
# print(singleton is new_singleton)
# print(singleton.l)
# print(new_singleton.l)
 
# singleton.singl_variable = "Singleton Variable"
# print(new_singleton.singl_variable)