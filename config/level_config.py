from levels.level_class import *


def create_levels(game):
    level_1 = Level()
    level_1.set_back(DIR_IMG + 'cave.png')
    level_1.load_back(game)
    level_1.set_hero(200, 350)
    level_1.min_x = 0
    level_1.max_x = WIN_X * 15
    # level_1.set_goal(3600, 180)
    game.levels.append(level_1)

