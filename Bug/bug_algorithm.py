import numpy as np 
#1. get the robot from the goal to start via the calculated m line
#2. combine bug 1 and 2
#3. bug 1 - The robot heads straight towards the goal until it hits an obstacle, then explores the whole obstacle, then finds the shortest path from the obstacle to the goal.
#4. bug 2 - the robot explores the obstacles until it finds a closer point to the goal (does not explore the whole obstacle)
#5. 2D grid
#6. obstacles - lets use shapes
#7. start and goal position
#8. strategy in combination: start off as bug 2 and if it gets stuck switch to bug 1 after finding a path switch to bug 2
#9.left hand rule
#10. bug 1 will keep track of the closest point to the obstacle as it is exploring it
#10. bug 2 will check if it crosses the mline then it will move foward to the goal
#11. end if reaches the goal or cant find a way to goal

def create_environment(rows, cols, obstacles):
    """
    param rows: number of rows in grid
    param cols: number of columns in grid
    param obstacles: number is obstacles in grid. tuple showing the position of tuple
    return: the 2d grid with ostacles placed
    """
    grid = np.zeros((rows,cols)) #new grid based on num of rows and col 0 meaning free space

    for obstacle in obstacles:
        grid[obstacle[0], obstacle[1]] = 1
    
    return grid

#obstacles = [(1, 1), (2, 1), (3, 1), (1, 3), (2, 3), (3, 3)]
#print(create_environment(5,5,obstacles))

        





