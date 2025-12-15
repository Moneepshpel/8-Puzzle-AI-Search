class Puzzle:
    def __init__(self, state):
        """
        state: list of 9 numbers (0 represents the empty tile)
        Example: [1, 2, 3, 4, 0, 5, 6, 7, 8]
        """
        self.state = state

    def is_solvable(self):
        """
        Check if the puzzle is solvable.
        """
        inversion_count = 0
        s = [num for num in self.state if num != 0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] > s[j]:
                    inversion_count += 1
        return inversion_count % 2 == 0

    def print_state(self):
        """Print the puzzle in 3x3 format."""
        for i in range(0, 9, 3):
            print(self.state[i:i+3])
        print()

    def move_tile(self, index1, index2):
        """Swap two tiles."""
        new_state = self.state[:]
        new_state[index1], new_state[index2] = new_state[index2], new_state[index1]
        return Puzzle(new_state)
