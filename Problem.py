import numpy as np 

class Problem:
    def __init__(self, init_state):
        self.initial_state = init_state
        self.current_state = init_state
        self.expand_count = 0
        self.size = 3
        self.goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
    
    #------------------GETTER----------------#
    def getInitState(self):
        return self.initial_state
    
    def getCurrentState(self):
        return self.current_state
    
    def getGoalState(self):
        return self.goal_state

    def getExpandCount(self):
        return self.expand_count

    def getLegalOps(self):
        indices = np.where(self.current_state == 0)
        moves = [indices[0][0], indices[1][0]]
        allMoves = []
        #Up
        if moves[0] > 0:
            allMoves.append(np.array([moves[0] - 1, moves[1]]))
        #Down
        if moves[0] < self.size - 1:
            allMoves.append(np.array([moves[0] + 1, moves[1]]))

        #Left
        if moves[1] > 0:
            allMoves.append(np.array([moves[0], moves[1] - 1]))

        #Right
        if moves[1] > self.size - 1:
            allMoves.append(np.array([moves[0], moves[1] + 1]))

        #print("Test ", allMoves[0], "Item ", self.initial_state[allMoves[0][0]][allMoves[0][1]])

        return allMoves

    #------------------SETTER----------------#
    def setInitState(self, matrix):
        self.init_state = matrix
        self.current_state = matrix

    #------------------PRINT-----------------#
    def print(self):
        for i in range (0,self.size):
            print(self.current_state[i])
    
    
