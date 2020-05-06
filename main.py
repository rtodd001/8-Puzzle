import numpy as np 
from Problem import *
from Heuristic import *
from Search import *
import heapq

size = 3
def defaultPuzzle():
    matrix = [[1,2,3],[4,8,0],[7,6,5]]
    return matrix

def menu():
    val = int(input("Welcome to 861228848 8 puzzle solver.\nType '1' to use a default puzzle, or '2' to enter your own puzzle.\n"))
    puzzle = []
    uniform = UniformHeur()
    misplace = MisplacedHeur()
    euclid = EuclidHeur()
    search = Search()
    if val == 1:
        puzzle = defaultPuzzle()
    elif val == 2:
        print("Enter your puzzle,use a zero to represent the blank")
        for i in range(0,size):
            x,y,z = input("Enter the row and use space or tabs between numbers ").split()
            puzzle.append([int(x),int(y),int(z)])
    
    problem = Problem(puzzle)
    choice = int(input("Enter your choice of algorithm\nUniform Cost Search\nA* with the Misplaced Tile heuristic.\nA* with the Euclidian distance heuristic\n"))
    if choice == 1:
        search.solve(problem, uniform)
    elif choice == 2:
        search.solve(problem, misplace)
    elif choice == 3:
        search.solve(problem, euclid)



def main():
    #problem.print()
    menu()

if __name__ == "__main__":
    main()