from board import Board


DIFFICULTIES = {
    "easy": {
        "rows": 6,
        "cols": 6,
        "mines": 6
    },
    "medium": {
        "rows": 8,
        "cols": 8,
        "mines": 12
    },
    "hard": {
        "rows": 10,
        "cols": 10,
        "mines": 20
    }
}


class Minesweeper:
    def __init__(self):
        self.board = None

    def choose_difficulty(self):
        while True:
            print()
            print("Choose difficulty:")
            print("1. Easy   - 6x6, 6 mines")
            print("2. Medium - 8x8, 12 mines")
            print("3. Hard   - 10x10, 20 mines")

            choice = input("> ").strip().lower()

            difficulty_map = {
                "1": "easy",
                "2": "medium",
                "3": "hard",
                "easy": "easy",
                "medium": "medium",
                "hard": "hard"
            }

            if choice not in difficulty_map:
                print("Invalid difficulty. Choose Easy, Medium, or Hard.")
                continue

            difficulty = difficulty_map[choice]
            settings = DIFFICULTIES[difficulty]

            rows = settings["rows"]
            cols = settings["cols"]
            mines = settings["mines"]

            if mines >= rows * cols:
                print("Invalid difficulty configuration.")
                continue

            return difficulty, settings

    def display(self, reveal_mines=False):
        b = self.board

        print()
        print("   " + " ".join(str(c + 1) for c in range(b.cols)))

        for r in range(b.rows):
            cells = []

            for c in range(b.cols):
                pos = (r, c)

                if reveal_mines and pos in b.mines:
                    ch = "*"
                elif pos in b.flags:
                    ch = "F"
                elif pos not in b.revealed:
                    ch = "#"
                elif pos in b.mines:
                    ch = "*"
                else:
                    ch = str(b.adjacent_mines(r, c))

                cells.append(ch)

            print(f"{r + 1:2} " + " ".join(cells))

    def run(self):
        print("Minesweeper")

        difficulty, settings = self.choose_difficulty()

        self.board = Board(
            rows=settings["rows"],
            cols=settings["cols"],
            mines=settings["mines"]
        )

        print()
        print(f"Difficulty: {difficulty.capitalize()}")
        print(
            f"Board: {self.board.rows}x{self.board.cols} | "
            f"Mines: {self.board.mine_total}"
        )
        print("Commands: r row col | f row col | q")

        while True:
            self.display()

            raw = input("> ").strip().lower()

            if raw == "q":
                return

            parts = raw.split()

            if len(parts) != 3 or parts[0] not in {"r", "f"}:
                print("Use r row col or f row col.")
                continue

            try:
                r = int(parts[1]) - 1
                c = int(parts[2]) - 1
            except ValueError:
                print("Coordinates must be numbers.")
                continue

            if not self.board.in_bounds(r, c):
                print("Outside the board.")
                continue

            if parts[0] == "f":
                changed = self.board.toggle_flag((r, c))

                if changed:
                    if (r, c) in self.board.flags:
                        print(f"Flagged ({r + 1}, {c + 1}).")
                    else:
                        print(f"Unflagged ({r + 1}, {c + 1}).")
                else:
                    print("Cannot flag a revealed cell.")

                continue

            hit_mine = self.board.reveal((r, c))

            print(f"Revealed ({r + 1}, {c + 1}).")

            if hit_mine:
                self.display(reveal_mines=True)
                print("BOOM! You hit a mine.")
                return

            if self.board.won():
                self.display()
                print("You cleared the board!")
                return