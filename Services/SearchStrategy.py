from abc import ABC, abstractmethod
import sys

sys.path.append("..")

from Model.PuzzleBoard import PuzzleBoard
from Model.Answer import Answer
from Services.BoardServices import BoardServices
from Services.FringeFactory import FringeFactory


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, initial_puzzle: PuzzleBoard, services: BoardServices) -> Answer:
        pass

    @staticmethod
    def _search_fringe(initial_puzzle: PuzzleBoard, services: BoardServices, fringe_type) -> Answer:
        nodes_expanded = 0
        max_depth = 0
        found = False
        explored_states = set([])
        fringe_factory = FringeFactory()
        fringe = fringe_factory.create_fringe(fringe_type)
        fringe.add_node(initial_puzzle, services)
        explored_states.add(tuple(initial_puzzle.get_state()))
        ans_board = None
        ans = Answer()
        while not fringe.is_empty():
            cur_board: PuzzleBoard = fringe.get_node()
            nodes_expanded += 1
            if services.is_goal(cur_board.get_state()):
                found = True
                ans_board = cur_board
                break
            for child in cur_board.get_children():
                if not tuple(child.get_state()) in explored_states:
                    fringe.add_node(child, services)
                    explored_states.add(tuple(child.get_state()))
                    max_depth = max(max_depth, child.get_depth())
        ans.add_answer_attr(ans_board, found, max_depth, nodes_expanded, fringe.get_size(), fringe.get_max_size())
        return ans


class DFSStrategy(SearchStrategy):

    def search(self, initial_puzzle: PuzzleBoard, services: BoardServices) -> Answer:
        return super()._search_fringe(initial_puzzle, services, "dfs")


class BFSStrategy(SearchStrategy):

    def search(self, initial_puzzle: PuzzleBoard, services: BoardServices) -> Answer:
        return super()._search_fringe(initial_puzzle, services, "bfs")


class AstarManhattanStrategy(SearchStrategy):

    def search(self, initial_puzzle: PuzzleBoard, services: BoardServices) -> Answer:
        return super()._search_fringe(initial_puzzle, services, "a*manhattan")


class AstarEuclidStrategy(SearchStrategy):

    def search(self, initial_puzzle: PuzzleBoard, services: BoardServices) -> Answer:
            return super()._search_fringe(initial_puzzle, services, "a*euclidean")
