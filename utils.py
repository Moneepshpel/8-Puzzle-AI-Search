# utils.py
# Utility functions and data structures used by all search algorithms

import heapq

# -------------------------
# Queue (for BFS)
# -------------------------
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# -------------------------
# Stack (for DFS)
# -------------------------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# -------------------------
# Priority Queue (UCS, Greedy, A*)
# -------------------------
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0   # to avoid comparison between nodes

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.count, item))
        self.count += 1

    def pop(self):
        return heapq.heappop(self.heap)[2]

    def is_empty(self):
        return len(self.heap) == 0


# -------------------------
# Heuristic Functions
# -------------------------

# Heuristic 1: Number of misplaced tiles
def misplaced_tiles(state, goal_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count


# Heuristic 2: Manhattan Distance (Admissible)
def manhattan_distance(state, goal_state):
    distance = 0

    goal_positions = {}
    for i in range(3):
        for j in range(3):
            goal_positions[goal_state[i][j]] = (i, j)

    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += abs(i - goal_i) + abs(j - goal_j)

    return distance
