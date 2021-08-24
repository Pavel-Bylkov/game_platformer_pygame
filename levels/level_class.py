import pygame as pg
from config.constants import *
from sprites.game_sprites_classes import Platform


def get_platform(x, y, w, h, length, x_speed, y_speed):
    area = pg.Rect(x, y, w, h)
    return (length, x, y, area, x_speed, y_speed)


class Level:
    """каждый экземпляр этого класса - это описание одного уровня
    для описания игры нужно в файле level_config создавать экземпляры Level()
    и добавлять в них методами add и set нужную информацию.
    """
    def __init__(self):
        self.platforms = []  # список аргументов для создания платформ
        self.enemies = []  # список аргументов для создания врагов
        self.goal = []  # цель уровня (картинка и координаты спрайта)
        self.hero_x = 0  # координаты, в которых появляется игрок
        self.hero_y = 0
        self.background_img = ""  # картинка фона уровня
        self.min_x = 0  # левая граница уровня
        self.max_x = 0  # правая граница уровня (герой дальше пройти не сможет)

    def set_back(self, filename):
        self.background_img = filename

    def add_platform(self, x, y, w, h, length, x_speed, y_speed):
        """добавляем в описание уровня платформу"""
        self.platforms.append([x, y, w, h, length, x_speed, y_speed])

    def add_enemy(self, enemy_type, x, y, x_min, x_max, x_speed):
        """тип врага будет определять, какая у него картинка"""
        self.enemies.append([enemy_type, x, y, x_min, x_max, x_speed])

    def set_hero(self, x, y):
        self.hero_x = x
        self.hero_y = y

    def set_goal(self, x, y):
        self.goal = [x, y]

    def load_back(self, game):
        game.set_back(self.background_img)

    def load_platforms(self, game):
        for p in self.platforms:
            pl = Platform(*get_platform(*p))  # pl = Platform(length, x, y, area, x_speed, y_speed)
            game.add_barrier(pl)

    def load_enemies(self, game):
        # img = generate_image(3, 3, C_WHITE) # Оставляем временно стандартную картинку
        img = game.costumes[gr_enemy]
        for enemy_info in self.enemies:
            # (enemy_type, x, y, x_min, x_max, x_speed)
            enemy_type = enemy_info[0]
            x, y, x_min, x_max, x_speed = enemy_info[1], enemy_info[2],\
                                          enemy_info[3], enemy_info[4], enemy_info[5]
            area = pg.Rect(x_min, 0, x_max - x_min, WIN_Y)
            if enemy_type == 1:
                e = Enemy2(img, x, y, area, x_speed=x_speed)
            else:
                e = Enemy1(img, x, y, area, x_speed=x_speed)
            game.enemies.add(e)
            game.all_sprites.add(e)

    def load_goal(self, game):
        game.add_goal(Goal(self.goal[0], self.goal[1]))

    def load_hero(self, game):
        # img = generate_image(3, 3, C_YELLOW) # Оставляем тут временно стандартную картинку для героя
        img = game.costumes[gr_hero]
        x = self.hero_x
        y = self.hero_y
        area = pg.Rect(self.min_x, -WIN_Y, self.max_x, 2 * WIN_Y)
        return Hero(img, x, y, area)

    def load(self, game):
        self.load_back(game)
        self.load_platforms(game)
        self.load_enemies(game)
        self.load_goal(game)
        return self.load_hero(game)
