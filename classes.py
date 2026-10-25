

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
        self.status = "unchecked"

    def toggle(self, text):
        
        if text == "flag":
            self.status = "FLAG" 
            return self.status

    def display(self):
        if self.status == "FLAG":
            return APPEARANCE["FLAG"]
        else:
            return APPEARANCE["COVERED"]

    def __repr__(self):
        return f"Cell{self.x, self.y}"

class Mine(Cell):
    def __init__(self, x, y):
        super().__init(x, y)
    
    def display(self):
        return APPEARANCE["MINE"]

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.create_board()

        self.num_mines = 0

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

    def toggle(self, x, y, status):
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

