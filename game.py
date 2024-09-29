from MenuScene import MenuScene
from core.game import Game

def main():
    Game.start(1000, 500)
    Game.set_scene(MenuScene(Game.screen))
    Game.run()


if __name__ == "__main__":
    main()
