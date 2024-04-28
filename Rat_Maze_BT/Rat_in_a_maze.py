import numpy as np
import random
import time
import copy

print("Welcome!!!\n")
time.sleep(1)

sol_maze = [] # to store the solution of the maze
symbol = 5

N = int(input("Enter size of maze: "))
print("\n")

def MAZE(maze):
    global solution
    solution = copy.deepcopy(maze)

    # When the solution is found then return 
    if BACKTRACKING_ALGORITHM(maze, 0, 0, solution) == False:
        return False
    return True

def BACKTRACKING_ALGORITHM(maze, x, y, solution):
    # The rat has reached the bottom-right corner of the maze.
    if x == N-1 and y == N-1:
        solution[x][y] = symbol
        return True

    # Checks whether the rat's move is valid or not
    if check(maze, x, y) == True:
        solution[x][y] = symbol

        # For going below
        if BACKTRACKING_ALGORITHM(maze, x+1, y, solution) == True:
            return True
            
        # For going right
        if BACKTRACKING_ALGORITHM(maze, x, y+1, solution) == True:
            return True
            
        # When neither condition is met
        solution[x][y] = 0
        return False
        
def check(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

while True:
    # The NxN maze consists of 0s and 1s.  
    maze = np.random.randint(0, 2, size=(N, N))
    # To check whether the generated maze is solvable or not 
    if MAZE(maze) == False or maze[N-1][N-1] == 0 or maze[0][0] == 0:
        continue

    time.sleep(1)
    for row in maze:
        for element in row:
            print(str(element), end=" ")
        print()
    time.sleep(1)
    print("\nThis is the maze to be solved")
    break

time.sleep(1)
ch = input(("\nEnter y to get solution: "))
print('\n')
if ch == 'y' or ch == 'Y':
    for row in solution:
        for element in row:
            print(str(element), end=" ")
        print()
print("\nThis is the solution maze")

            
        