import pygame as pg

from game import *

game = Game()
game.start()

while game.run:
    # Ввод данных (обработка событий)
    for event in pg.event.get():
        # событие нажатия на крестик окошка
        if event.type == pg.QUIT:
            game.stop()  # цикл перестанет повторяться, программа завершится

    pg.display.update()
    # Пауза
    game.timer.tick(FPS)
