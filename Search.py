import heapq
import numpy as np

class Search:
    def solve(self, problem, heuristic):
        counter = 0
        maxSize = -1
        frontier = []
        heapq.heappush(frontier,(0, problem.getInitState()))
        print ("Expanding state")
        problem.print()
        #for i in range(0,2):
        while True:
            #do something
            #0: Cost
            #1: Puzzle

            item = heapq.heappop(frontier)
            hn = heuristic.calculate(item[1], problem.getGoalState())
            print("The best state to expand with g(n) = {} and h(n) = {} is…".format(item[0] - hn, hn))
            problem.setCurrentState(item[1])
            problem.print()
            print("Expanding this node")
            counter += 1
            #print("Front: ", frontier)
            #print(item[0], item[1])
    
            if(np.array_equal(item[1], problem.getGoalState())):
                problem.setCurrentState(item[1])
                print("GOAL!!!")
                print("To solve this problem the search algorithm expanded a total of {} nodes.\nThe maximum number of nodes in the queue at any one time: {}.".format(counter, maxSize))
                break
            #returns all the possible moves
            options = problem.getLegalOps(item[1])
            #iterate through all the posible moves
            #This is the expansion of the removed node
            for one in options:
                #create a new matrix with the new possible move
                possibility = problem.moveTile(item[1], one)
                problem.setCurrentState(possibility)
                cost = item[0] + 1 + heuristic.calculate(possibility, problem.getGoalState())
                heapq.heappush(frontier,(cost, possibility))
            maxSize = max(maxSize, len(frontier))
                
            

