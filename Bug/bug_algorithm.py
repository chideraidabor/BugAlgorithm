import numpy as np 
import matplotlib.pyplot as plt
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

start = (0,0)
goal = (4,4)
rectangle_obstacles = [(1,1,3,1), # rec 1 - position 1,1 with width of 3 and height of 1
                       (4,4,2,2)] # rec 2 - position 3,3 with width of 2 and height of 2
l_obstacles = [(2, 2, 1, 3), #circle 1 - center position at 2,2 with a radius of 1
               (2, 2, 3, 1)] #circle 2 - center position at 4,1 with a radius of 2

def create_environment(rows, cols, rectangle_obstacles, l_obstacles):
    """
    param rows: number of rows in grid
    param cols: number of columns in grid
    param rectangle_obstacles: tuple showing the position of the rectangle
    return: the 2d grid with ostacles placed
    """
    grid = np.zeros((rows,cols)) #new grid based on num of rows and col 0 meaning free space

    for rect in rectangle_obstacles:
        top_left_row, top_left_col, width, height = rect
        for i in range(top_left_row, top_left_row + height):
            for j in range(top_left_col, top_left_col + width):
                if i < rows and j < cols:
                    grid[i,j] = 1

    for l_shape in l_obstacles:
        top_left_row, top_left_col, width, height = l_shape
        for i in range(top_left_row, top_left_row + height):
            for j in range(top_left_col, top_left_col + width):
                if i < rows and j < cols:
                    grid[i, j] = 1

    return grid

def visualize_env(grid):
    plt.imshow(grid,cmap="gray_r")
    plt.title("Environment")
    plt.grid(True)
    plt.show()

#create_environment(6, 6, rectangle_obstacles, circle_obstacles) 
visualize_env(create_environment(6,6,rectangle_obstacles, l_obstacles))       





