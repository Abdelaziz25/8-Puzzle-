import sys
sys.path.append("..")

from Model.PuzzleBoard import PuzzleBoard
from Model.Answer import Answer
from Services.BoardServices import BoardServices
from Services.SearchStrategy import SearchStrategy

from typing import List


class SearchAgent(object):

    __search_strategy: SearchStrategy
    __answer: Answer
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(BoardServices, cls).__new__(cls)
    #     return cls.instance

    def set_initial_puzzle(self, initial_state):
        self.__initial_puzzle = PuzzleBoard(initial_state)

    def set_board_services(self, length, width):
        self.__board_services = BoardServices()
        self.__board_services.set_board_dim(length, width)

    def set_search_strategy(self, search_strategy: SearchStrategy):
        self.__search_strategy = search_strategy

    def __add_path_ans(self):
        if self.__answer.found:
            cur_board = self.__answer.puzzle_sol
            steps = [cur_board.get_prev_step()]
            states = [cur_board.get_state()]
            while cur_board.get_parent() is not None:
                cur_board = cur_board.get_parent()
                print(cur_board.get_prev_step)
                steps.append(cur_board.get_prev_step)
                states.append(cur_board.get_state)
            steps.reverse()
            states.reverse()
            self.__answer.add_path_step(steps)
            self.__answer.add_path_states(states)


    def solvePuzzle(self):
        self.__answer = self.__search_strategy.search(self.__initial_puzzle, self.__board_services)
        # print()
        self.__add_path_ans()
        return self.__answer


