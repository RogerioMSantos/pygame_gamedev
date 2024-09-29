def set_menu_scene():
    from MenuScene import MenuScene
    from core.game import Game
    Game.set_scene(MenuScene(Game.screen))

def set_main_scene():
    from MainScene import MainScene
    from core.game import Game
    Game.set_scene(MainScene(Game.screen))