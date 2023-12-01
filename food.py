import random

class Food:
    def __init__(self, game_board):
        self.game_board = game_board
        self.position = self.spawn_food()

    def spawn_food(self):
        # Logic for spawning food at a random location
        pass
