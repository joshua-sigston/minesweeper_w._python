import random
from re import X


APPEARANCE = {
    "COVERED": ".",
    "CHECKED": "0",
    "FLAG": "F",
    "MINE": "*"
}

DIRECTIONS =[
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_flagged = False
        self.appearance = "."


    # toggle function to change the display of a none mine cell
    def toggle(self, text, num=None):
        if text == "flag":
            self.is_flagged = not self.is_flagged
        else:
            if num > 0 or not None:
                self.appearance = num

    def display(self):
        if self.is_flagged:
            return APPEARANCE["FLAG"]
        else:
            return self.appearance

    def __repr__(self):
        return f"Cell{self.x, self.y}"

# mine cell, position to be predetermined when user selects board size
class Mine(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.found = False
        self.flagged = False

    def toggle(self, status):
        # if user flags mine, does not end game. If use checks flagged mine, removes flag and ends game
        if status == "check":
            if self.flagged:
                self.flagged = not self.flagged
                self.found = not self.found
            else:
                self.found = not self.found
        elif status == "flag":
            self.flagged = not self.flagged
        else:
            self.found = False
    
    def display(self):
        if self.found:
            return APPEARANCE["MINE"]
        elif self.flagged:
            return APPEARANCE["FLAG"]
        else:
            return APPEARANCE["COVERED"]

    def __repr__(self):
        return f"Cell{self.x, self.y} {self.flagged}"

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mines_discovered = False

        self.create_board()

        self.num_of_mines = 0

        self.mine_coordinates = []
        self.num_neighbor_mines = None

        self.x = None
        self.y = None

    def in_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def create_mines(self):
        r = self.rows
        c = self.cols

        max_num_of_mines = (r * c * 40) // 100
        num_of_mines = random.randint(0, max_num_of_mines)
        spots = [(row, col) for row in range(r) for col in range(c)]
        for r, c in random.sample(spots, num_of_mines):
            x = r
            y = c
            self.mine_coordinates.append((x, y))
            self.grid[x][y] = Mine(x, y)
        return self.mine_coordinates, num_of_mines

    def create_board(self):
        grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(Cell(r, c))
            grid.append(row)
        
        self.grid = grid

    def display_board(self):
        print(" ", end=" ")
        print(" ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            print(r, end=" ")
            for c in range(self.cols):
                print(self.grid[r][c].display(), end=" ")
            print()

        # if user flags mine, does not end game. If use checks flagged mine, removes flag and ends game
        if (self.x, self.y) in self.mine_coordinates:
            if self.grid[self.x][self.y].flagged:
                return
            else:
                self.mines_discovered = True
                print("You stepped on a mine! GAME OVER")
                return self.mines_discovered

    # check neighbors for mines, count the number of mines and display that number on the cell checks
    #  get neighbor coordinates
    def get_neighbor_coordinates(self, x, y):
        neighbors = []
        for dr, dc in DIRECTIONS:
            #  adds dr to x
            nr = x + dr
            #  adds dc to y
            nc = y + dc
            if self.in_bounds(nr, nc):
                neighbors.append((nr, nc))
        return neighbors

    # if neighbor is a mine, do not add to list of neighbors to run recursison on
    def filter_neighbors(self, neighbors):
        filtered_list = []
        for x, y in neighbors:
            cell = self.grid[x][y]
            if isinstance(cell, Mine):
                continue
            else:
                filtered_list.append((x, y))
        return filtered_list

    def reveal(self, x, y):
        cell = self.grid[x][y]
        # already opened, flagged or a mine: stop
        if cell.is_flagged or cell.appearance != ".":
            return

        # create a list of neighbors
        neighbors = self.get_neighbor_coordinates(x, y)
        # filter out neighbors that are not mines
        safe = self.filter_neighbors(neighbors)
        # change appearance of cell to the number of mines arround it
        count = len(neighbors) - len(safe)
        cell.appearance = count
        
        # if count = 0 recurssion.
        if count == 0:
            for nx, ny in safe:
                self.reveal(nx, ny)

    # funciton passes to Cell in order to change display of cell
    def toggle(self, x, y, status):
        if not self.in_bounds(x, y):
            print("Those numbers are off the board.")
            return

        cell = self.grid[x][y]

        self.x = x
        self.y = y

        if status == "flag":
            # flip the flag on this cell, whether it is a mine or not
            cell.toggle(status)
            # stop here so a flag does not open the cell
            return
        # the command is check, and this cell is a mine
        elif isinstance(cell, Mine):
            # toggles mine found to be True, game over
            self.grid[x][y].toggle(status)
        else:
            # check on a safe cell: open it, and continue only when its count is 0
            self.reveal(x, y)
            
    def __repr__(self):
        return f"Board{self.rows, self.cols}"


# if __name__ == "__main__":
    # c = Cell(0, 0)
    # print(c.display())
    # print(c)
    # b = Board(10, 10)
    # print(b)
    # b.create_board()
    # b.display_board()