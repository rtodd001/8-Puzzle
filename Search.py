import heapq
import numpy as np
from Node import *
import sys

class Search:
    def solve(self, problem, heuristic):
        counter = 0
        uni = False
        if heuristic.calculate(problem.getInitState(), problem.getGoalState()) == 0:
            uni = True
        maxCost = sys.maxsize
        visited = {}
        #visit_Costs = []
        foundCount = 0
        maxQueueSize = -1
        frontier = []
        node = Node(problem.getInitState(),1)
        #print("Cost", node.getCost())
        heapq.heappush(frontier,(node.getCost(), node))
        #visited[str(problem.getInitState())] = [node.getCost()]
        print ("Expanding state", visited)
        problem.print()
        while True:
            #do something
            #0: Cost
            #1: Puzzle
            if len(frontier) == 0:
                print("GOAL!!!")
                print("To solve this problem the search algorithm expanded a total of {} nodes.\nThe maximum number of nodes in the queue at any one time: {}.".format(counter, maxQueueSize))
                break

            item = heapq.heappop(frontier)
            if np.array_equal(item[1].getMatrix(), problem.getGoalState()):
                if uni:
                    print("GOAL!!!")
                    print("To solve this problem the search algorithm expanded a total of {} nodes.\nThe maximum number of nodes in the queue at any one time: {}.".format(counter, maxQueueSize))
                    break
                else:
                    maxCost = item[0]
                    continue
            if str(item[1].getMatrix()) in visited:
                continue
            if maxCost < item[0]:
                continue
            allCosts = []
            if str(item[1].getMatrix()) in visited:
                hold = visited.get(str(item[1].getMatrix()))
                allCosts.extend(hold)
            else:
                allCosts = [item[0]]
            #print("Costs ", allCosts)
            visited[str(item[1].getMatrix())] = allCosts
            #print("Visit ", visited)
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
                maxCost = item[0]
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
            maxQueueSize = max(maxQueueSize, len(frontier))
                
            

