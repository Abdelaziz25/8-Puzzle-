import random
from Model.PuzzleBoard import PuzzleBoard
from Services.BoardServices import BoardServices
from Services.SearchAgent import SearchAgent
from Services.SearchStrategy import SearchStrategy, DFSStrategy, BFSStrategy, AstarEuclidStrategy, AstarManhattanStrategy
from Model.Answer import Answer

class Controller:

    __ans: Answer

    def __init__(self, length=3, width=3):
        self.__search_agent = SearchAgent()
        self.initialState2d = [[0,0,0],[0,0,0],[0,0,0]]


    def set_puzzle_for_agent(self, initial_state2d, length, width):
        initial_state = []
        self.initialState2d = initial_state2d
        for i in range(length):
            for j in range(width):
                initial_state.append(initial_state2d[i][j])

        self.__search_agent.set_board_services(length, width)
        self.__search_agent.set_initial_puzzle(initial_state, length, width)

    def __agent_solve(self, search_strategy: SearchStrategy):
        self.__search_agent.set_search_strategy(search_strategy)

        self.__ans = self.__search_agent.solvePuzzle()

    def search(self, stringMethod):
        if stringMethod == "DFS":
            self.__agent_solve(DFSStrategy())
        elif stringMethod == "BFS":
            self.__agent_solve(BFSStrategy())
        elif stringMethod == "AsMan":
            self.__agent_solve(AstarManhattanStrategy())
        elif stringMethod == "AsEc":
            self.__agent_solve(AstarEuclidStrategy())


        print("is found ", self.__ans.found)
        if self.__ans.found:
            print(self.__ans.steps)
            print("cost ",self.__ans.sol_cost)
            print("nodes expanded ", self.__ans.no_nodes_exp)
            print("max depth ",self.__ans.max_depth)


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


    def getpath(self):
        if not self.__ans.found:
            return []
        steps = self.__ans.steps
        path = []
        izero=0
        jzero=0

        for i in range(3):
            for j in range(3):
                if self.initialState2d[i][j] == 0:
                    path.append( (i,j) )
                    izero = i
                    jzero = j
                    break
            if len(path)!= 0:
                break
        print(izero, " ", jzero)

        for step in steps:
            if step == 'Up':
                izero-= 1
            elif step == 'Down':
                izero+= 1
            elif step == 'Right':
                jzero += 1
            elif step == 'Left':
                jzero -= 1
            print(izero, " ", jzero)

            if izero<0 or izero>2 or jzero<0 or jzero>2 :
                print("EEERRRRROOOOOOOOORRRRRRRR")
            else:
                path.append((izero, jzero))

        return path

    def getstates(self):
        if not self.__ans.found:
            return [["Cost of path", "NA"],["Nodes expanded", "NA"],["Search depth", "NA"],["Running time","NA"]]
        dec = []
        dec.append(["Cost of path", self.__ans.sol_cost])
        dec.append(["Nodes expanded", self.__ans.no_nodes_exp])
        dec.append(["Search depth", self.__ans.max_depth])
        dec.append(["Running time",self.__ans.time])
        return dec

    #Method that solves the problem


""""
sa = SearchAgent()
sa.set_board_services(3, 3)
sa.set_search_strategy(BFSStrategy())
# sa.set_initial_puzzle([1,2,5,3,4,0,6,7,8])
sa.set_initial_puzzle([1,4,2,6,5,8,7,3,0])
# sa.set_initial_puzzle([3,1,2, 0, 4,5,6,7,8])
# print([x for x in sa.solvePuzzle().steps])
print(sa.solvePuzzle().steps)
print(sa.solvePuzzle().puzzle_sol.get_depth())
print(sa.solvePuzzle().found)



# pb = PuzzleBoard([1,2,3,4,8,5,6,7,0])
# ps = BoardServices()
# ps.set_board_dim(3, 3)
# print(pb.get_state().index(0))
# tpp = ps.get_children(pb)
# for xxx in tpp:
#     print(xxx.get_state())
# for i, x in enumerate([11,22,33]):
#     print(f"i {i} x {x}")

"""