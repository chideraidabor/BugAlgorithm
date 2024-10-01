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

#start and goal
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

def create_m_line(start, goal, rows, cols):
    m_line = []
    x1,y1 = start
    x2,y2 = goal

    num_steps = max(abs(x2 - x1), abs(y2 - y1))

    for i in range(num_steps + 1):
        t = i / num_steps
        x = int(x1 + t * (x2 - x1))
        y = int(y1 + t * (y2 - y1))
        m_line.append((x, y))#store the cordinate in the mline array with the cordinates of steps to the goal
        #return an array of stepf for the mline
    return m_line

def bug2(start, goal, grid):
    #.shape gets the number of rows and columns
    m_line = create_m_line(start, goal, grid.shape[0], grid.shape[1])
    robot_position = start
    path = [robot_position]# a list of all the coordinates taken to the goal

    for next_step in m_line:
        if grid[next_step[0], next_step[1]] == 1: #if an obstacle detected
            print(f"Obstacle encountered at {next_step}, switching to boundary following.")
            #boundary following code
            break
        else:
            robot_position = next_step
            path.append(robot_position)
            print(f"Moving to {robot_position}")

        if robot_position == goal:
            print("Goal Reached!")
            break
    return path

def follow_boundary_bug_2(grid, position):
    row,col = position
    #direction = 




grid = create_environment(6, 6, rectangle_obstacles, l_obstacles)

visualize_env(grid)

path = bug2(start, goal, grid)

print("Path followed by bug 2:", path)




