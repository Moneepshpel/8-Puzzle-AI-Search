# 8-Puzzle AI Project Report & Summary

## Project Name
8-Puzzle Solver using AI Algorithms

## Introduction
The 8-Puzzle is a classic sliding puzzle consisting of a 3x3 board with 8 numbered tiles and one empty space. The goal is to move tiles to reach a target configuration.

## Objectives
- Solve the 8-Puzzle using AI algorithms.
- Compare performance in terms of steps, memory usage, and execution time.

## Algorithms Used

### 1. Breadth-First Search (BFS)
- Explores all nodes at the current depth before moving deeper.
- Guarantees the shortest solution.

### 2. Depth-First Search (DFS)
- Explores as deep as possible along each branch before backtracking.
- May not find the shortest path and can use less memory.

### 3. Uniform Cost Search (UCS)
- Expands the node with the lowest path cost.
- Guarantees optimal solution if cost is uniform.

### 4 . Greedy Search

Uses a heuristic to select the node that seems closest to the goal.

Does not guarantee the shortest path, but often faster than BFS or DFS.

Common heuristics: misplaced tiles, Manhattan distance 

### 5. A* Search
- Uses heuristics to estimate the cost to goal.
- More efficient; finds the optimal solution faster.
- Common heuristics: misplaced tiles, Manhattan distance.

## Project Structure
8-Puzzle-AI/

bfs.py

dfs.py

ucs.py

greedy.py 

a_star.py

puzzle.py

utils.py

## Performance Comparison
- **BFS:** shortest path, high memory usage.
- **DFS:** may take longer, less memory.
- **UCS:** optimal, slower than A*.
- **Greedy:** usually faster than BFS and DFS, uses heuristic to guide search, does not guarantee the shortest path, memory usage moderate.
- **A*:** fastest, optimal with good heuristic.

## Summary

The 8-Puzzle project successfully implements multiple AI search algorithms to solve the puzzle. The algorithms include:  

- **Breadth-First Search (BFS):** guarantees the shortest path but consumes high memory.  
- **Depth-First Search (DFS):** uses less memory, may take longer, and does not guarantee the shortest solution.  
- **Uniform Cost Search (UCS):** finds the optimal solution by expanding nodes based on path cost; slower than A*.  
- **Greedy Search:** uses heuristics to guide the search, usually faster than BFS and DFS, but does **not guarantee the shortest path**; memory usage is moderate.  
- **A* Search:** combines path cost and heuristic, finds the optimal solution efficiently and often faster than UCS and BFS.  

This README provides a complete overview of the project, including objectives, algorithm explanations, project structure, and performance comparison. It allows anyone to understand how different AI algorithms perform on the 8-Puzzle and to compare their efficiency, memory usage, and solution optimality.


## Conclusion
This README serves both as the **main report** and **summary** for the project. It is fully viewable on GitHub, making additional PDF files optional. Any visitor can read the entire report directly without downloading extra files.

## How to Run the Algorithms

To run the 8-Puzzle algorithms, make sure all files are in the same folder:

### 1. Breadth-First Search (BFS)
python bfs.py

### 2. Depth-First Search (DFS)
python dfs.py

### 3. Uniform Cost Search (UCS)
python ucs.py

### 4. Greedy Search
python greedy.py

### 5. A* Search
python astar.py

