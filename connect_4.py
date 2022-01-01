class Board:

    def __init__(self, size: int):
        if size < 4:
            raise ValueError("Size of board must be at least 4 rows by 4 cols")

        self.size = size
        self.clear_state()

    def move(self, col: int, player: int) -> int:
        if not self._num_empty:
            raise ValueError("No more empty places in the board")
        elif not 0 <= col < self.size:
            raise IndexError("Choice is out of bounds")
        elif self._grid[0][col]:
            raise ValueError("Column is full")
        elif not 1 <= player <= 2:
            raise ValueError("Player must be either 1 or 2")

        # Find the greatest row where there is a zero in the specified column.
        drop_row = 0
        for row in range(self.size):
            if self._grid[row][col]:
                break

            drop_row = row

        self._grid[drop_row][col] = player
        self._num_empty -= 1

        print(self)

        if self._check_winner(drop_row, col, player):
            print(f"Game has been won by player {player}")
            print("Resetting game state")
            self.clear_state()

    def clear_state(self):
        self._grid = [[0] * self.size for _ in range(self.size)]
        self._num_empty = self.size ** 2

    def _check_winner(self, row: int, col: int, player: int):
        return (self._check_horizontal(row, col, player)
                or self._check_vertical(row, col, player)
                or self._check_diagonal(row, col, player)
                or self._check_anti_diagonal(row, col, player))

    def _check_horizontal(self, row: int, col: int, player: int):
        # Check for 4 of the same player in the row around the current move.
        num_in_row = 1
        for adj_col in range(col + 1, self.size):
            if self._grid[row][adj_col] != player:
                break

            num_in_row += 1
            if num_in_row == 4:
                return True

        for adj_col in range(col - 1, -1, -1):
            if self._grid[row][adj_col] != player:
                break

            num_in_row += 1
            if num_in_row == 4:
                return True

        return False

    def _check_vertical(self, row, col, player):
        num_in_col = 1
        for adj_row in range(row + 1, self.size):
            if self._grid[adj_row][col] != player:
                break

            num_in_col += 1
            if num_in_col == 4:
                return True

        for adj_row in range(col - 1, -1, -1):
            if self._grid[adj_row][col] != player:
                break

            num_in_col += 1
            if num_in_col == 4:
                return True

        return False

    def _check_diagonal(self, row, col, player):
        num_diagonal = 1

        curr_row, curr_col = row + 1, col - 1
        while curr_row < self.size and curr_col >= 0:
            if self._grid[curr_row][curr_col] != player:
                break

            num_diagonal += 1
            if num_diagonal == 4:
                return True

            curr_row += 1
            curr_col -= 1

        curr_row, curr_col = row - 1, col + 1
        while curr_row >= 0 and curr_col < self.size:
            if self._grid[curr_row][curr_col] != player:
                break

            num_diagonal += 1
            if num_diagonal == 4:
                return True

            curr_row -= 1
            curr_col += 1

        return False

    def _check_anti_diagonal(self, row, col, player):
        num_anti_diagonal = 1

        curr_row, curr_col = row + 1, col + 1
        while curr_row < self.size and curr_col < self.size:
            if self._grid[curr_row][curr_col] != player:
                break

            num_anti_diagonal += 1
            if num_anti_diagonal == 4:
                return True

            curr_row += 1
            curr_col += 1

        curr_row, curr_col = row - 1, col - 1
        while curr_row >= 0 and curr_col >= 0:
            if self._grid[curr_row][curr_col] != player:
                break

            num_anti_diagonal += 1
            if num_anti_diagonal == 4:
                return True

            curr_row -= 1
            curr_col -= 1

        return False

    def __str__(self):
        return "\n".join(str(row) for row in self._grid) + "\n"

    def __repr__(self):
        return f"Board(n={len(self._grid)})"


game = Board(10)
game.move(3, 2)
game.move(3, 1)
game.move(2, 1)
game.move(4, 2)
game.move(4, 2)
game.move(4, 2)
game.move(4, 2)

game.move(5, 2)
game.move(6, 2)
game.move(6, 2)
game.move(7, 2)
game.move(7, 2)
game.move(7, 2)
game.move(8, 1)
game.move(8, 2)
game.move(8, 2)
game.move(8, 2)

game.move(5, 1)
game.move(5, 2)
game.move(5, 2)
game.move(5, 2)
game.move(6, 2)
game.move(6, 2)
game.move(6, 2)
game.move(7, 2)
game.move(7, 2)
game.move(8, 2)
