from game_board import GameBoard
from snake import Snake
from food import Food
from collision import CollisionDetector
from score import Score
from game_over import handle_game_over

class Menu:
    def __init__(self):
        self.game_board = GameBoard()
        self.snake = Snake(self.game_board)
        self.food = Food(self.game_board)
        self.collision_detector = CollisionDetector(self.game_board, self.snake)
        self.score = Score()

    def show_main_menu(self):
        # Main menu logic here
        pass

    def start_game(self):
        # Game loop logic here
        pass

    def view_instructions(self):
        # Display instructions logic here
        pass

    def exit_game(self):
        sys.exit()
