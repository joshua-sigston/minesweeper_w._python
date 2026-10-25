import random


APPEARANCE = {
    "COVERED": ".",
    "CHECKED": "0",
    "FLAG": "F",
    "MINE": "*"
}


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_flagged = False


    # toggle function to change the display of a none mine cell
    def toggle(self, text): 
        if text == "flag":
            self.is_flagged = not self.is_flagged

    def display(self):
        if self.is_flagged:
            return APPEARANCE["FLAG"]
        else:
            return APPEARANCE["COVERED"]

    def __repr__(self):
        return f"Cell{self.x, self.y}"

# mine cell, position to be predetermined when user selects board size
class Mine(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def display(self):
        return APPEARANCE["MINE"]

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.create_board()

        self.num_mines = 0

    def in_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    # def create_mines(self):
    #     r = self.rows
    #     c = self.cols

    #     mine_coordinates = []

    #     num_of_mines = (r * c * 40) // 100
    #     number_of_mines_to_place = random.randint(0, num_of_mines)
    #     spots = [(row, col) for row in range(r) for col in range(c)]
    #     for row, col in random.sample(spots, number_of_mines_to_place):
    #         mine_coordinates.append((row, col))
    #     return mine_coordinates, num_of_mines

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


    # funciton passes to Cell in order to change display of cell
    def toggle(self, x, y, status):
        if not self.in_bounds(x, y):
            print("Those numbers are off the board.")
            return

        self.grid[x][y].toggle(status)

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