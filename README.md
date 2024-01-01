# Pathfinding Visualizer

This is a pathfinding visualizer built using Pygame. The idea is to visualize the A* pathfinding algorithm in a basic grid world. User can manually set the start and end points, create obstacles, and generate a random maze to see how the A* algorithm finds the shortest path.


## Usage

To start the visualizer, run the `main.py` script:


- Left click to create walls (obstacles) and set start and end points.
- Right click to remove walls or points.
- Press 'Space' to start the pathfinding.
- Press 'M' to generate a random maze. (to be updated)

## Structure

- `src/astar.py`: Contains the implementation of the A* pathfinding algorithm.
- `src/grid.py`: Manages the grid and nodes for pathfinding.
- `src/main.py`: Main script to run the Pygame visualizer.
- `src/settings.py`: Configuration settings for the visualizer.
