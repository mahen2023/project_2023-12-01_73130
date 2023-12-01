class GameBoard:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = self.create_grid()

    def create_grid(self):
        return [[None for _ in range(self.width)] for _ in range(self.height)]

    def reset_board(self):
        self.grid = self.create_grid()
