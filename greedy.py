import heapq

# Define the target configuration (Goal State)
# 0 represents the empty space (blank tile)
GOAL_STATE = (1, 2, 3, 4, 5, 6, 0, 7, 8)

def manhattan_distance(state):
    """
    Heuristic Function: Calculates the sum of Manhattan distances 
    of tiles from their correct goal positions.
    """
    distance = 0
    for i in range(len(state)):
        tile = state[i]
        if tile != 0:
            # Current coordinates in 3x3 grid
            curr_row, curr_col = divmod(i, 3)
            # Goal coordinates for this specific tile
            goal_idx = GOAL_STATE.index(tile)
            goal_row, goal_col = divmod(goal_idx, 3)
            # Sum of absolute differences (Vertical + Horizontal)
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

def get_neighbors(state):
    """Generates all possible board configurations from the current state."""
    neighbors = []
    state_list = list(state)
    zero_idx = state_list.index(0)
    row, col = divmod(zero_idx, 3)

    # Moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = state_list[:]
            # Swap empty space with the adjacent tile
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_greedy(start_state):
    """Solves the puzzle using Greedy Best-First Search."""
    # Priority Queue stores: (heuristic_score, current_state, path_taken)
    # Greedy only looks at the Heuristic score h(n)
    priority_queue = [(manhattan_distance(start_state), start_state, [])]
    visited = {start_state}

    while priority_queue:
        # Pop the state that "appears" to be closest to the goal
        h_score, current_state, path = heapq.heappop(priority_queue)

        # Check if Goal is reached
        if current_state == GOAL_STATE:
            return path + [current_state]

        # Expand neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                # Calculate h(n) for the neighbor
                h_neighbor = manhattan_distance(neighbor)
                heapq.heappush(priority_queue, (h_neighbor, neighbor, path + [current_state]))
                
    return None

def display_board(state):
    """Prints the board in a 3x3 format."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("-" * 15)

# --- Execution ---

# Example starting state:
initial_state = (1, 0, 3, 4, 2, 6, 7, 5, 8)

print("Searching for solution using Greedy BFS...")
solution_path = solve_greedy(initial_state)

if solution_path:
    print(f"Success! Found solution in {len(solution_path) - 1} steps:")
    for step in solution_path:
        display_board(step)
else:
    print("No solution found.")
