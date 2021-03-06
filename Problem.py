import numpy as np 

class Problem:
    def __init__(self, init_state):
        self.initial_state = init_state
        self.current_state = init_state
        self.expand_count = 0
        self.size = 3
        self.goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])

    #------------------SETTER----------------#
    def setInitState(self, matrix):
        self.init_state = matrix
        self.current_state = matrix
    
    def setCurrentState(self, matrix):
        self.current_state = matrix

    #------------------GETTER----------------#
    def getInitState(self):
        return self.initial_state
    
    def getCurrentState(self):
        return self.current_state
    
    def getGoalState(self):
        return self.goal_state

    def getExpandCount(self):
        return self.expand_count

    #return a numpy array with all possible moves
    #values represent the location the 0 can go
    def getLegalOps(self, matrix):
        #arr = np.array(self.current_state)
        arr = np.array(matrix)
        indices = np.where(arr == 0)
        #print("Indices", indices)
        moves = [indices[0][0], indices[1][0]]
        allMoves = []

        #Up
        if moves[0] > 0:
            allMoves.append([moves[0] - 1, moves[1]])
        #Down
        if moves[0] < self.size - 1:
            allMoves.append([moves[0] + 1, moves[1]])

        #Left
        if moves[1] > 0:
            allMoves.append([moves[0], moves[1] - 1])

        #Right
        if moves[1] < self.size - 1:
            allMoves.append([moves[0], moves[1] + 1])

        #print("Test ", allMoves[0], "Item ", self.initial_state[allMoves[0][0]][allMoves[0][1]])
        return allMoves

    #----------------FUNCTIONS---------------#
    def moveTile(self, matrix, position):
        arr = np.array(matrix)
        indices = np.where(arr == 0)
        #location of the 0 tile
        moves = [indices[0][0], indices[1][0]]
        #The item that we are going to swap
        update = arr[position[0], position[1]]
        arr[position[0], position[1]] = 0
        arr[moves[0], moves[1]] = update
        return arr.tolist()



    #------------------PRINT-----------------#
    def print(self):
        for row in self.current_state:
            for col in row:
                print(col, end = " ")
            print()
