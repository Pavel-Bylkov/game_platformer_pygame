import pygame as pg

from config.constants import *
from sprites.game_sprites_classes import COSTUMES, WINDOW


class Camera:
    def __init__(self):
        self.rect = pg.Rect(0, 0, WIN_X, WIN_Y)
        # положение камеры относительно всего большого уровня (может влиять на рисунок фона)

    def move(self, offset_x, offset_y, group):
        """смещение камеры относительно уровня"""
        self.rect.move_ip(-1 * offset_x, -1 * offset_y)
        for s in group:
            s.rect.move_ip(offset_x, offset_y)
            s.area.move_ip(offset_x, offset_y)

    def back_shift(self):
        """возвращает число от 0 до WIN_X, на которое по оси X надо сдвинуть фон"""
        # return self.rect.x % WIN_X
        # попробуем сдвигать фон в 2 раза медленнее, чем движется камера.
        # тогда должна возникнуть глубина:
        return (self.rect.x // 2) % WIN_X


class Game:
    def __init__(self):
        self.run = True
        # список всех персонажей игры:
        self.all_sprites = pg.sprite.Group()
        # список опор (платформ):
        self.barriers = pg.sprite.Group()
        # список врагов:
        self.enemies = pg.sprite.Group()
        # список снарядов героя (убивают врагов):
        self.fires = pg.sprite.Group()
        # список целей (переключают на следующий уровень):
        self.goals = pg.sprite.Group()
        # в игре одна камера, из которой смотрим:
        self.camera = Camera()
        self.hero_pos = pg.Rect(0, 0, 0, 0)  # здесь запоминаем место героя на предыдущем цикле
        # список уровней игры:
        self.levels = []  # этот список заполнится при загрузке уровней (level_config)
        self.current_level = -1
        # список используемых костюмов:
        self.costumes = []
        # переменные для числа очков и жизней:
        self.lives = HERO_START_LIVES
        self.points = 0

    def start(self):
        self.timer = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.window = WINDOW
        self.costumes = COSTUMES
        # self.help = Help()
        self.is_help = False
        self.is_finished = False
        # self.music = Music()
        self.back_image = pg.Surface([WIN_X, WIN_Y])
        self.back_image.fill(C_GREEN)  # по умолчанию фон - зелёный прямоугольник

    def stop(self):
        self.run = False

    def start_level(self, level_n):
        self.current_level = level_n
        hero_of_the_level = self.levels[level_n].load()
        self.all_sprites.add(hero_of_the_level)
        self.hero_pos = hero_of_the_level.rect.copy()  # copy() нужна для копирования сложных объектов

        return hero_of_the_level  # возвращает спрайт героя

    def set_back(self, filename=""):
        if len(filename) > 0:  # если в уровне не прописан фон, то соотв. свойство - пустая строка
            self.back_image = pg.transform.scale(
                pg.image.load(filename).convert(), [WIN_X, WIN_Y])
        else:
            self.back_image = pg.Surface([WIN_X, WIN_Y])
            self.back_image.fill(C_GREEN)  # по умолчанию фон - зелёный прямоугольник

    def draw_back(self, x=0, y=0):
        """заливает окно фоновым изображением"""
        self.window.blit(self.back_image, (x, y))

    def draw_back_with_shift(self):
        local_shift = self.camera.back_shift()
        self.draw_back(local_shift)
        if local_shift != 0:
            # сдвиг на 1 пиксел позволяет некоторые картинки "склеить" лучше
            self.draw_back(local_shift - WIN_X + 1)

    def add_barrier(self, platform):
        self.barriers.add(platform)
        self.all_sprites.add(platform)

