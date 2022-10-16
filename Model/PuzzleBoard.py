from typing import List


class PuzzleBoard:

    def __init__(self, state: List[int], parent = None, prev_step = "", depth: int = 0):
        self.__state = state
        self.__parent = parent
        self.__prev_step = prev_step
        self.__depth = depth
        # print(self.__prev_step)

    def get_parent(self):
        return self.__parent

    def get_prev_step(self):
        # print(self.__prev_step)
        return self.__prev_step

    def get_depth(self):
        return self.__depth

    def get_state(self) -> List[int]:
        return self.__state
    

