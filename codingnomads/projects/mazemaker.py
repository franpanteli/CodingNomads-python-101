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
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)
    return maze