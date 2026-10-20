
# Task 6: More on Classes - Tic-Tac-Toe


class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right"
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.turn = "X"

    def __str__(self):
        lines = []

        lines.append(
            f" {self.board_array[0][0]} | "
            f"{self.board_array[0][1]} | "
            f"{self.board_array[0][2]} \n"
        )

        lines.append("-----------\n")

        lines.append(
            f" {self.board_array[1][0]} | "
            f"{self.board_array[1][1]} | "
            f"{self.board_array[1][2]} \n"
        )

        lines.append("-----------\n")

        lines.append(
            f" {self.board_array[2][0]} | "
            f"{self.board_array[2][1]} | "
            f"{self.board_array[2][2]} \n"
        )

        return "".join(lines)

    def move(self, move_string):
        # Check whether the move is valid
        if move_string not in Board.valid_moves:
            raise TictactoeException(
                "That's not a valid move."
            )

        # Convert the move name to row and column
        move_index = Board.valid_moves.index(move_string)

        row = move_index // 3
        column = move_index % 3

        # Check whether the spot is already taken
        if self.board_array[row][column] != " ":
            raise TictactoeException(
                "That spot is taken."
            )

        # Place X or O on the board
        self.board_array[row][column] = self.turn

        # Switch turns
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        # Check rows
        for row in range(3):
            if (
                self.board_array[row][0] != " "
                and self.board_array[row][0]
                == self.board_array[row][1]
                == self.board_array[row][2]
            ):
                winner = self.board_array[row][0]
                return (True, f"{winner} wins!")

        # Check columns
        for column in range(3):
            if (
                self.board_array[0][column] != " "
                and self.board_array[0][column]
                == self.board_array[1][column]
                == self.board_array[2][column]
            ):
                winner = self.board_array[0][column]
                return (True, f"{winner} wins!")

        # Check diagonals
        if (
            self.board_array[1][1] != " "
            and self.board_array[0][0]
            == self.board_array[1][1]
            == self.board_array[2][2]
        ):
            winner = self.board_array[1][1]
            return (True, f"{winner} wins!")

        if (
            self.board_array[1][1] != " "
            and self.board_array[0][2]
            == self.board_array[1][1]
            == self.board_array[2][0]
        ):
            winner = self.board_array[1][1]
            return (True, f"{winner} wins!")

        # Check whether the board is full
        board_full = all(
            cell != " "
            for row in self.board_array
            for cell in row
        )

        if board_full:
            return (True, "Cat's Game.")

        # Game continues
        return (False, f"{self.turn}'s turn.")


# Task 6: Play the game
board = Board()

print("Welcome to Tic-Tac-Toe!")
print("Enter moves such as 'upper left', 'center', or 'lower right'.")
print()

while True:
    print(board)

    game_over, message = board.whats_next()

    if game_over:
        print(message)
        break

    move_string = input(
        f"{board.turn}'s turn. Enter your move: "
    ).strip().lower()

    try:
        board.move(move_string)
    except TictactoeException as error:
        print(error.message)
        print("Please try again.")
