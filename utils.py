def get_neighbors(state):
    """
    Return a list of neighbor states from the current state.
    """
    neighbors = []
    zero_index = state.index(0)
    swaps = []
    # Left
    if zero_index % 3 > 0:
        swaps.append(-1)
    # Right
    if zero_index % 3 < 2:
        swaps.append(1)
    # Up
    if zero_index // 3 > 0:
        swaps.append(-3)
    # Down
    if zero_index // 3 < 2:
        swaps.append(3)

    for s in swaps:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index + s] = new_state[zero_index + s], new_state[zero_index]
        neighbors.append(new_state)

    return neighbors

def manhattan_distance(state, goal):
    """Heuristic: sum of Manhattan distances of tiles from their goal positions."""
    distance = 0
    for num in range(1, 9):
        idx_state = state.index(num)
        idx_goal = goal.index(num)
        x1, y1 = divmod(idx_state, 3)
        x2, y2 = divmod(idx_goal, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
