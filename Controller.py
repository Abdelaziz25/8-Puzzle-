import random
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