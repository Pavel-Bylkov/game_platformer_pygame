import pygame as pg

from config.constants import *
from levels.level_class import *
from config.level_config import *
from game import *

game = Game()

game.start()
create_levels(game)
# hero = game.start_level(0)

while game.run:
    # Ввод данных (обработка событий)
    for event in pg.event.get():
        # событие нажатия на крестик окошка
        if event.type == pg.QUIT:
            game.stop()  # цикл перестанет повторяться, программа завершится

    # Вывод данных (отрисовка)
    game.draw_back_with_shift()

    pg.display.update()
    # Пауза
    game.timer.tick(FPS)
