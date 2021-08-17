import pygame as pg

from sprites.base_class import BaseSprite, Character


class Platform(BaseSprite):
    """класс для платформы - это BaseSprite с изображением платформы,
    растянутым на нужно число клеток.
    """
    def __init__(self, length, x, y, area, x_speed=0, y_speed=0):
        """получает длину платформы, генерирует нужной длины картинку"""
        img_l = game.costumes[gr_plat_l]
        img_m = game.costumes[gr_plat_m]
        img_r = game.costumes[gr_plat_r]
        image = append_img3(img_l, img_m, img_r, length)

        # создаем BaseSprite с нужным
        super().__init__(image, x, y, area, x_speed=x_speed, y_speed=y_speed)


class Goal(BaseSprite):
    """класс для цели - это BaseSprite"""
    pass


class Fire(Character):
    """Снаряды - могут двигаться, как платформы
    при этом получат возможность анимации, если её прописать в Character
    умирают, пролетев определенное расстояние"""
    pass


class Actor(Character):
    """персонажи, которые могут действовать сами (в отличие от снарядов)"""
    pass


class Hero(Actor):
    """Главный персонаж. Умирает от врагов.
    Снаряды добавляет в список, убивающий врагов."""
    pass


class Enemy(Actor):
    """Полноценный персонаж.
    Прописывается в список врагов. Его снаряды прописываются в список врагов.
    Умирает от снарядов героя."""
    pass


class Enemy1(Enemy):
    """враг вида 1, умеет стрелять"""
    pass


class Enemy2(Enemy):
    """враг вида 2, не умеет стрелять"""
    pass
