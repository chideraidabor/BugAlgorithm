import matplotlib.pyplot as plt
import numpy as np

def create_environment():
    grid = np.zeros((6, 6))
    # Creating a simple obstacle that the robot can navigate around
    grid[2:4, 2] = 1  # Vertical obstacle in the middle
    return grid

def plot_environment(grid, start, goal, path=None, m_line=None):
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='gray', origin='upper')
    ax.plot(start[1], start[0], 'gs', label='Start')  # Start position
    ax.plot(goal[1], goal[0], 'r*', label='Goal')  # Goal position
    
    if m_line is not None:
        ax.plot([start[1], goal[1]], [start[0], goal[0]], 'r--', label='M-line')
    
    if path is not None:
        path = np.array(path)
        ax.plot(path[:, 1], path[:, 0], 'bo-', label='Robot Path')
    
    ax.set_title("Robot Movement Environment")
    ax.legend()
    plt.gca().invert_yaxis()
    plt.show()

def bug2_algorithm(grid, start, goal, max_steps=150):
    direction = np.array(goal) - np.array(start)
    direction = direction / np.linalg.norm(direction)  # Normalize to get unit vector
    
    position = np.array(start)
    path = [tuple(position)]
    steps = 0

    while steps < max_steps:
        # Calculate next position towards M-line
        next_position = position + direction
        next_position = np.round(next_position).astype(int)
        
        # Check if next position is within bounds
        if (0 <= next_position[0] < grid.shape[0]) and (0 <= next_position[1] < grid.shape[1]):
            # Check if next position is an obstacle
            if grid[next_position[0], next_position[1]] == 1:
                print(f"Obstacle at {tuple(next_position)}, following boundary.")
                # Follow boundary (simple logic: try moving right or down)
                if grid[position[0], (position[1] + 1) % grid.shape[1]] == 0:
                    position[1] = (position[1] + 1) % grid.shape[1]
                elif grid[(position[0] + 1) % grid.shape[0], position[1]] == 0:
                    position[0] = (position[0] + 1) % grid.shape[0]
                else:
                    print("Robot is stuck, no valid moves.")
                    break
            else:
                # Move towards the goal along the M-line
                position = next_position
        else:
            print("Next position is out of bounds, stopping.")
            break
        
        path.append(tuple(position))
        steps += 1
        print(f"Step {steps}: Moved to {tuple(position)}")
        
        # Check if goal is reached
        if np.array_equal(position, goal):
            print("Goal reached!")
            break
    
    if steps == max_steps:
        print("Failed to reach goal after maximum steps.")
    
    return path

def main():
    grid = create_environment()
    start = (0, 0)
    goal = (4, 4)
    
    # Plot initial environment with M-line
    plot_environment(grid, start, goal, m_line=True)
    
    # Run Bug2 algorithm
    path = bug2_algorithm(grid, start, goal)
    
    # Plot the final path taken by the robot
    plot_environment(grid, start, goal, path=path, m_line=True)

if __name__ == "__main__":
    main()