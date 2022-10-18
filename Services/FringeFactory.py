import sys
sys.path.append("..")

from Model.Fringe import Fringe, EuclideanFringe, DFSFringe, BFSFringe, ManhattanFringe


class FringeFactory:

    @staticmethod
    def create_fringe(strategy: str) -> Fringe:
        if strategy == "dfs":
            return DFSFringe()
        elif strategy == "bfs":
            return BFSFringe()
        elif strategy == "a*manhattan":
            print(strategy)
            return ManhattanFringe()
        elif strategy == "a*euclidean":
            print(strategy)
            return EuclideanFringe()
        return None