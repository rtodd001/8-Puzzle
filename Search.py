import heapq
import numpy as np

class Search:
    def solve(self, problem, heuristic):
        counter = 0
        frontier = []
        heapq.heappush(frontier,(0, problem.getInitState()))
        #for i in range(0,2):
        while True:
            #do something
            #0: Cost
            #1: Puzzle
            item = heapq.heappop(frontier)
            print("Front: ", frontier)
            print(item[0], item[1])
    
            if(np.array_equal(item[1], problem.getGoalState())):
                print("Done!")
                break
            #returns all the possible moves
            options = problem.getLegalOps(item[1])
            #iterate through all the posible moves
            #This is the expansion of the removed node
            for one in options:
                #create a new matrix with the new possible move
                possibility = problem.moveTile(item[1], one)
                problem.setCurrentState(possibility)
                problem.print()
                cost = one[0] + 1 + heuristic.calculate(possibility, problem.getGoalState())
                print(cost)
                heapq.heappush(frontier,(cost, possibility))
                
            

