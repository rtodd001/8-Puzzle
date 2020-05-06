import numpy as np 
from Problem import *
from Heuristic import *
from Search import *
import heapq

size = 3
def defaultPuzzle(difficulty):
    #matrix = [[1,2,3],[4,8,0],[7,6,5]]
    #Trivial
    if difficulty == 1:
        matrix = [[1,2,3],[4,5,6],[7,8,0]]
    #Very Easy
    elif difficulty == 2:
        matrix = [[1,2,3],[4,5,6],[7,0,8]]
    #Easy
    elif difficulty == 3:
        matrix = [[1,2,0],[4,5,3],[7,8,6]]
    #doable
    elif difficulty == 4:
        matrix = [[0,1,2],[4,5,3],[7,8,6]]
    #Oh Boy
    elif difficulty == 5:
        matrix = [[8,7,1],[6,0,2],[5,4,3]]
    #Impossible
    elif difficulty == 6:    
        matrix = [[1,2,3],[4,5,6],[8,7,0]]

    return matrix

def menu():
    val = int(input("Welcome to 861228848 8 puzzle solver.\nType '1' to use a default puzzle, or '2' to enter your own puzzle.\n"))
    puzzle = []
    uniform = UniformHeur()
    misplace = MisplacedHeur()
    euclid = EuclidHeur()
    search = Search()
    if val == 1:
        difficulty = int(input("Enter the difficulty level:\n1:Trivial\n2:Very Easy\n3:Easy\n4:doable\n5:Oh Boy\n6:Impossible\n"))
        puzzle = defaultPuzzle(difficulty)
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