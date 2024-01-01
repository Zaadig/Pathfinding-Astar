import sys
sys.path.append('./src') 

from astar import astar

def main():
    # Simple maze (2D grid)
    # 0 - free path, 1 - obstacle
    maze = [[0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0]]

    start = (0, 0)  # Start position
    end = (4, 5)    # End position

    # Find the path using A* algorithm
    path = astar(maze, start, end)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
