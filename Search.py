import heapq
import numpy as np
from Node import *

class Search:
    def solve(self, problem, heuristic):
        counter = 0
        foundCount = 0
        maxSize = -1
        frontier = []
        node = Node(problem.getInitState(),1)
        print("Cost", node.getCost())
        heapq.heappush(frontier,(node.getCost(), node))
        print ("Expanding state")
        problem.print()
        while True:
            #do something
            #0: Cost
            #1: Puzzle

            item = heapq.heappop(frontier)
            #print("Node ", item)
            hn = heuristic.calculate(item[1].getMatrix(), problem.getGoalState())
            print("The best state to expand with g(n) = {} and h(n) = {} is…".format(item[1].getDepth(), hn))
            problem.setCurrentState(item[1].getMatrix())
            problem.print()
            print("Expanding this node")
            counter += 1
            #print("Front: ", frontier)
            #print(item[0], item[1])
    
            if(np.array_equal(item[1].getMatrix(), problem.getGoalState())):
                problem.setCurrentState(item[1].getMatrix())
                print("GOAL!!!")
                print("To solve this problem the search algorithm expanded a total of {} nodes.\nThe maximum number of nodes in the queue at any one time: {}.".format(counter, maxSize))
                break
            #returns all the possible moves
            options = problem.getLegalOps(item[1].getMatrix())

            #iterate through all the posible moves
            #This is the expansion of the removed node
            for one in options:
                #create a new matrix with the new possible move
                possibility = problem.moveTile(item[1].getMatrix(), one)
                temp = Node(possibility, item[1].getDepth())
                temp.setDepth(item[1].getDepth() + 1)
                problem.setCurrentState(possibility)
                cost = temp.getDepth() + heuristic.calculate(possibility, problem.getGoalState())
                temp.setCost(cost)
                #print("Cost: ", temp.getCost())
                heapq.heappush(frontier,(temp.getCost(), temp))
            print("Done")
            """ for index in frontier:
                print(index[0], index[1]) """
            maxSize = max(maxSize, len(frontier))
                
            

