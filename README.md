# A* Pathfinding Visualization

This repository contains implementation and visualization of the A* algorithm, designed to find the most efficient path from start to goal in a 2D grid with obstacles.

## Modules Description

- **`A_star.py`**: Implements the A* algorithm using Python. It includes methods for setting up the environment, calculating heuristics, and navigating through the grid.

- **`env.py`**: Sets up the grid environment for the A* algorithm. It specifies grid boundaries, obstacle placements, and valid motion directions for the agent.

- **`plotting.py`**: Handles the visualization of the grid, path, and the process of pathfinding using matplotlib. It shows the start, goal, obstacles, and the path determined by A*.

## How to Run

1. **Installation**: Ensure Python 3.x is installed along with matplotlib and numpy.
2. pip install matplotlib numpy

3. **Running the script**:
4. python A_star.py

## Features

- Customizable grid size and obstacle configuration.
- Visualization of the pathfinding process, including explored nodes and the final path.
- Different heuristic options (Manhattan, Euclidean) to influence pathfinding behavior.

## Output

The script will display a series of matplotlib plots illustrating the steps the A* algorithm takes to find the shortest path from start to goal, highlighting both the open set and closed set of nodes.

## Additional Information

- The grid and obstacle configurations can be modified in `env.py`.
- Heuristic function can be switched between "manhattan" and "euclidean" by changing the `heuristic_type` parameter in `A_star.py`.
