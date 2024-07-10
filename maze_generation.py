#GPT CODE
import random

def generate_maze(width, height):
    # Create a grid filled with walls ('#')
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Initialize starting point 'S'
    maze[1][1] = 'S'  # Starting point

    # Choose a random boundary position for the goal 'G'
    boundary_positions = [(0, random.randint(1, width - 2)), 
                          (height - 1, random.randint(1, width - 2)),
                          (random.randint(1, height - 2), 0),
                          (random.randint(1, height - 2), width - 1)]
    
    gx, gy = random.choice(boundary_positions)
    maze[gx][gy] = 'G'  # Goal

    # Depth-First Search (DFS) function to generate paths
    def dfs(x, y):
        # Directions for four possible moves (up, down, left, right)
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(directions)  # Randomize the order of directions

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == '#':
                # Carve a path
                maze[(x + nx) // 2][(y + ny) // 2] = ' '  # Remove wall between current and next cell
                maze[nx][ny] = ' '  # Mark the next cell as part of the path
                dfs(nx, ny)  # Recursively explore from the next cell

    # Start DFS from the starting point
    dfs(1, 1)

    # Ensure there are openings between the middle boundaries
    for i in range(2, width - 2, 2):
        maze[height // 2][i] = ' '
    for j in range(2, height - 2, 2):
        maze[j][width // 2] = ' '

    return maze