import curses
from curses import wrapper
import queue
import time
from maze_generation import *

maze = generate_maze(11, 11)

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def find_target(maze, target):
    for i, row in enumerate(maze):
        for j,val in enumerate(row):
            if val == target:
                return i, j
    return None

def find_path(stdsrc, maze):
    start = "S"
    goal = "G"
    start_pos = find_target(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdsrc.clear()
        print_maze(stdsrc, maze, path)
        time.sleep(.2)
        stdsrc.refresh()

        if maze[row][col] == goal:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for n in neighbors:
            if n in visited:
                continue
            r, c = n

            if maze[r][c] == "#":
                continue
            
            new_path = path + [n]
            q.put((n, new_path))
            visited.add(n)
        
def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col +1 < len(maze[0]):
        neighbors.append((row, col + 1))
    return neighbors

def print_maze(stdsrc, maze, path=[]):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)
    YELLOW = curses.color_pair(3)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if(i, j) in path:
                stdsrc.addstr(i, j*2, "X", YELLOW)
            elif value == "G":
                stdsrc.addstr(i, j*2, "G", GREEN)
            else:
                stdsrc.addstr(i, j*2, value, RED)

def main(stdsrc):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    find_path(stdsrc, maze)
    stdsrc.getkey()

wrapper(main)