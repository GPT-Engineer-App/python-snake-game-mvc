from model import SnakeGameModel
from view import SnakeGameView
from controller import SnakeGameController

def main():
    model = SnakeGameModel()
    view = SnakeGameView(model)
    controller = SnakeGameController(model, view)
    controller.run()

if __name__ == "__main__":
    main()