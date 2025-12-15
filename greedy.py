from queue import PriorityQueue

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Manhattan Distance Heuristic
def manhattan(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal_state.index(state[i])
            distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))

    return neighbors

def greedy(start_state):
    pq = PriorityQueue()
    pq.put((manhattan(start_state), start_state))

    visited = set()

    while not pq.empty():
        h, current = pq.get()

        if current == goal_state:
            print("Goal reached!")
            return True

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                pq.put((manhattan(neighbor), neighbor))

    print("No solution found")
    return False

if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    greedy(start)
