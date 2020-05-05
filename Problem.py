import numpy as np 

class Problem:
    def __init__(self, init_state):
        self.initial_state = init_state
        self.current_state = init_state
        self.expand_count = 0
        self.size = 3
        self.goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
    
    #------------------GETTER----------------#
    def getCurrentState(self):
        return self.current_state
    
    def getGoalState(self):
        return self.goal_state

    def getExpandCount(self):
        return self.expand_count

    def getLegalOps(self):
        indices = np.where(self.current_state == 0)
        #TO-DO
        #Get all the legal operations as a tuple

    #------------------SETTER----------------#
    def setInitState(self, matrix):
        self.init_state = matrix
        self.current_state = matrix

    #---------------FUNCTIONS----------------#
    def uniformHeuristic(self):
        return 0 

    #NEED TO FINISH WRITING getLegalOps() first
    def euclidHeuristic(self):
        distance = (np.subtract(np.where(self.goal_state == num), np.where(self.current_state == num)))
        return abs(distance[1][0]) + abs(distance[0][0])

    def misplacedHeuristic(self,num):


    #------------------PRINT-----------------#
    def print(self):
        for i in range (0,self.size):
            print(self.current_state[i])
    
    
