import random
from Model.PuzzleBoard import PuzzleBoard
from Services.BoardServices import BoardServices
from Services.SearchAgent import SearchAgent
from Services.SearchStrategy import SearchStrategy, DFSStrategy, BFSStrategy, AstarEuclidStrategy, AstarManhattanStrategy

class Controller:


    def createRandom(self):
        arr = [0,1,2,3,4,5,6,7,8]
        self.startstate = []
        for i in range(3):
            self.startstate.append([])
            for j in range(3):
                index = random.randint(0, len(arr)-1)
                self.startstate[i].append(arr[index])
                arr.remove(arr[index])

        return self.startstate

    def check(self, arr):
        if len(arr) != 3:
            return False

        dp = [0]*9
        for i in range(3):
            if len(arr[i]) != 3:
                return False
            for j in range(3):
                if dp[arr[i][j]] != 0:
                    return False
                dp[arr[i][j]] = 1

        return True


    def getpath(self, arr):
        return [(0,0),(0,1),(1,1),(1,0),(0,0)]

    def getstates(self):
        dec = []
        dec.append(["cost of path", 5])
        dec.append(["nodes expanded", 12])
        dec.append(["space depth", 100])
        dec.append(["running time", "1000 ms"])
        return dec


sa = SearchAgent()
sa.set_board_services(3, 3)
sa.set_search_strategy(AstarEuclidStrategy())
# sa.set_initial_puzzle([1,2,5,3,4,0,6,7,8])
sa.set_initial_puzzle([1,4,2,6,5,8,7,3,0])
# sa.set_initial_puzzle([3,1,2, 0, 4,5,6,7,8])
# print([x for x in sa.solvePuzzle().steps])
print(sa.solvePuzzle().puzzle_sol.get_depth())

# pb = PuzzleBoard([1,2,3,4,8,5,6,7,0])
# ps = BoardServices()
# ps.set_board_dim(3, 3)
# print(pb.get_state().index(0))
# tpp = ps.get_children(pb)
# for xxx in tpp:
#     print(xxx.get_state())
# for i, x in enumerate([11,22,33]):
#     print(f"i {i} x {x}")