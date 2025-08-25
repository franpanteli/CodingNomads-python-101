# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e


"""
    -> building a maze with an entrance and exit
    -> Randomised Prim's algorithm for creating a maze
        -> Start with a grid full of walls
        -> Pick a cell, start it as part of the maze
            -> Add the walls of the cell to the walls of the maze
        -> While there are walls in the list
            -> Pick a random wall from the list
            -> If one of the two cells that the wall divides is visited, then
                    -> Make the wall a package and mark the unvisited wall as part of the maze
                    -> Remove the wall from the list
    """


#to create the maze
cell = 'c' #parts of the maze are cells and walls
wall = 'w'

#this function creates an empty maze
def init_maze(width, height):
    maze = [] #initialise the maze as an empty list
    for i in range(0, height): #iterate through the cells until the height of the maze and join the cells together
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)
    return maze

#creating a function to print the maze - to distinguish walls from cells
from colorama import init, Fore #using the calorima module
# colorama needs to be initialized in order to be used
init()
def print_maze(maze): #this function is defined to print the maze
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('\n')


"""height=11 and width=27 outputs:
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
u u u u u u u u u u u u u u u u u u u u u u u u u u u
"""

#randomly picking the starting points
"""
    -> picking a point in the maze and initialising it as a free spot
"""

starting_height = int(random.random()*height)
starting_width = int(random.random()*width)

#to not start on a block that is on the edge of the maze
if starting_height == 0:
    starting_height += 1
if starting_height == height-1:
    starting_height -= 1
if starting_width == 0:
    starting_width += 1
if starting_width == width-1:
    starting_width -= 1

#marking this block as the surrounding path and adding the surrounding walls to the walls list
maze[starting_height][starting_width] = cell #this defines the cell for the maze
walls = [] #initialising the walls list
walls.append([starting_height-1, starting_width]) #adding each of the four walls to the walls list
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])

#the blocks around the starting cell are walls
maze[starting_height-1][starting_width] = wall #there are four walls around the maze
maze[starting_height][starting_width-1] = wall
maze[starting_height][starting_width+1] = wall
maze[starting_height+1][starting_width] = wall

#while there are walls in the list, pick a random wall from the list
while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]

#implementing the condition that if only one of the two cells that the wall divides is visited
"""
    -> checking the surrounding cells of the walls we are implementing
    -> we are checking the different ways a cell could be divided by a wall
    -> we need to check the walls to the left and right of the wall we are processing
    -> case 1: we check the blocks to the left and the right of the wall
    -> case 2: we check the blocks above and below the wall
    -> there are two conditions per wall, which makes (times four walls around the maze), eight different conditions to check
"""

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'u') and (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
   if (maze[rand_wall[0]-1][rand_wall[1]] == 'u') and (maze[rand_wall[0]+1][rand_wall[1]+1] == 'c'):
   if (maze[rand_wall[0]+1][rand_wall[1]] == 'u') and (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
   if (maze[rand_wall[0]][rand_wall[1]+1] == 'u') and (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

"""
    -> this accesses elements using indices
    -> adding checks for this:
"""

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]
    if rand_wall[1] != 0:
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u') and (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
    if rand_wall[0] != 0:
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'u') and (maze[rand_wall[0]+1][rand_wall[1]+1] == 'c'):
    if rand_wall[0] != height-1:
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'u') and (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
    if rand_wall[1] != width-1:
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'u') and (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

#building a function
"""
    -> if the four conditions holds, we want to make the wall a package and mark the unvisited cell as part of the maze
    -> every wall we are going to turn into a passage can't have more than one wall around it
        -> this is for the avoidance of passage clusters
    -> we need to check that the cell doesn't have more than two cells around it
    -> this code defines a function to check this
"""
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1
    return s_cells

#this incorporates that code in the main function
while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]
    if rand_wall[1] != 0:
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u') and (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:

"""
    -> we have only added the extra code in the first case
    -> the first applies for the rest
    -> the next part of the code turns the surrounding walls to maze
"""

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]
if rand_wall[1] != 0:
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u') and (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

"""
    -> this adds one of the surrounding walls
    -> we want to check if we are trying to access an invalid access and that we are not already adding existing walls to the list
    -> adding the neighbouring walls of the cell to the list and then continuing onto the next iteration
    -> we are defining a delete wall function for this
"""

def delete_wall(rand_wall):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

"""
    -> we are adding this function to the code
    -> if the wall we are processing doesn't ƒall into any of the cases we already have, it needs to get deleted from the list
    -> this is achieved by iterating through the wall int he list with a while loop
"""

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]
if rand_wall[1] != 0:
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u') and (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])
            delete_wall(rand_wall)
            continue
        continue

#some of the cells are unvisited if the list of walls is empty - this code makes them walls:
def make_walls(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = 'w'

#creating a maze entrance and exit
def create_entrance_exit(width, height):
    for i in range(0, width):
        if (maze[1][i] == 'c'):
            maze[0][i] = 'c'
            break
    for i in range(width-1, 0, -1):
        if (maze[height-2][i] == 'c'):
            maze[height-1][i] = 'c'
            break