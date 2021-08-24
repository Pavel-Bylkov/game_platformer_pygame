from levels.level_class import *


def create_levels(game):
    level_1 = Level()
    level_1.set_back(DIR_IMG + 'cave.png')
    level_1.load_back(game)  # временно
    level_1.set_hero(200, 350)
    level_1.min_x = 0
    level_1.max_x = WIN_X * 15
    level_1.add_platform(500, 50, 500, 250, 5, 0, 0)
    level_1.add_platform(x=300, y=150, w=500, h=550, length=6, x_speed=0, y_speed=2)
    level_1.add_platform(50, 500, 500, 250, 10, 3, 0)
    level_1.load_platforms(game)  # временно
    # level_1.set_goal(3600, 180)
    game.levels.append(level_1)

