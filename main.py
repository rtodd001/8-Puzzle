import numpy as np 
from Problem import *
from Heuristic import *

size = 3

def printPuzzle(matrix):
    for i in range (0,size):
        print(matrix[i])

def defaultPuzzle():
    matrix = np.array([[1,2,3],[4,8,0],[7,6,5]])
    return matrix

def menu():
    val = int(input("Welcome to 861228848 8 puzzle solver.\nType '1' to use a default puzzle, or '2' to enter your own puzzle.\n"))
    puzzle = []
    if val == 1:
        return defaultPuzzle()
    elif val == 2:
        print("Enter your puzzle,use a zero to represent the blank")
        #FIX ISSUE HERE WHERE THE INPUTTED ARRAY ARE NOT INTS
        for i in range(0,size):
            x,y,z = input("Enter the row and use space or tabs between numbers ").split()
            
            puzzle.append([int(x),int(y),int(z)])
        return puzzle



def main():
    problem = Problem(menu())
    problem.print()
    #print(problem.getGoalState())
    moves = problem.getLegalOps()
    print(moves)

    uniform = UniformHeur()
    misplace = MisplacedHeur()
    euclid = EuclidHeur()
    #print(misplace.calculate(problem.getInitState(), problem.getGoalState()))
    #print(euclid.calculate(problem.getInitState(), problem.getGoalState()))
    #print(uniform.calculate(problem.getInitState(), problem.getGoalState()))

if __name__ == "__main__":
    main()