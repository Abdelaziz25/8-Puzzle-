import heapq
from abc import ABC, abstractmethod
import sys
from typing import List, Tuple
from queue import Queue

sys.path.append("..")

from Model.PuzzleBoard import PuzzleBoard
from Services.BoardServices import BoardServices


class Fringe(ABC):
    @abstractmethod
    def get_node(self) -> PuzzleBoard:
        pass

    @abstractmethod
    def add_node(self, val: PuzzleBoard, services: BoardServices) -> None:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_max_size(self) -> int:
        pass


class DFSFringe(Fringe):

    def __init__(self):
        self.__stack: List[PuzzleBoard] = []
        self.__max_size = 0

    def get_node(self) -> PuzzleBoard:
        return self.__stack.pop()

    def add_node(self, val: PuzzleBoard, services: BoardServices = None) -> None:
        self.__stack.append(val)
        self.__max_size = max(self.get_size(), self.__max_size)

    def get_size(self) -> int:
        return len(self.__stack)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def get_max_size(self):
        return self.__max_size

class BFSFringe(Fringe):

    def __init__(self):
        self.__q: Queue[PuzzleBoard] = Queue()
        self.__max_size = 0

    def get_node(self) -> PuzzleBoard:
        return self.__q.get()

    def add_node(self, val: PuzzleBoard, services: BoardServices = None) -> None:
        self.__q.put(val)
        self.__max_size = max(self.get_size(), self.__max_size)

    def get_size(self) -> int:
        return self.__q.qsize()

    def is_empty(self) -> bool:
        return self.__q.empty()

    def get_max_size(self):
        return self.__max_size

class ManhattanFringe(Fringe):

    def __init__(self):
        self.__pq: List[Tuple[int, int, PuzzleBoard]] = []
        self.__max_size = 0
        self.__buff = 0

    def get_node(self) -> PuzzleBoard:
        _, _, ans = heapq.heappop(self.__pq)
        return ans

    def add_node(self, val: PuzzleBoard, services: BoardServices = None) -> None:
        self.__buff += 1
        heapq.heappush(self.__pq, (services.manhattan_h(val.get_state()) + 1, self.__buff, val))
        self.__max_size = max(self.get_size(), self.__max_size)

    def get_size(self) -> int:
        return len(self.__pq)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def get_max_size(self):
        return self.__max_size


class EuclideanFringe(Fringe):

    def __init__(self):
        self.__pq: List[Tuple[int, int, PuzzleBoard]] = []
        self.__max_size = 0
        self.__buff = 0

    def get_node(self) -> PuzzleBoard:
        _, _, ans = heapq.heappop(self.__pq)
        return ans

    def add_node(self, val: PuzzleBoard, services: BoardServices = None) -> None:
        self.__buff += 1
        heapq.heappush(self.__pq, (services.euclidean_h(val.get_state()) + 1, self.__buff, val))
        self.__max_size = max(self.get_size(), self.__max_size)

    def get_size(self) -> int:
        return len(self.__pq)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def get_max_size(self):
        return self.__max_size
