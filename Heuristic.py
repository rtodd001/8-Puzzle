import numpy as np

class Heuristic:
    def calculate(self, curr_state, goal_state):
        return 0

#this will use the above hardcoded h(n) to 0
class UniformHeur(Heuristic):
    pass

#calculate the number of misplaced tiles
class MisplacedHeur(Heuristic):
    def calculate(self, curr_state, goal_state):
        return np.count_nonzero(curr_state != goal_state)

class EuclidHeur(Heuristic):
    def calculate(self, curr_state, goal_state):
        totalDist = 0
        for i in range(len(curr_state)*len(curr_state)):
            dist = (np.subtract(np.where(goal_state == i), np.where(curr_state == i)))
            totalDist += abs(dist[1][0]) + abs(dist[0][0])
        return totalDist
