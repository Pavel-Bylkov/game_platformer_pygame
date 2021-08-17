"""Функции для загрузки и обработки изображений"""
import pygame as pg


def crop_img(filename, size):
    """обрезает картинку, оставляя только одну из непрозрачных частей,
    и устанавливает масштаб size %
    """
    img = pg.image.load(filename).convert_alpha()
    # взяв маску изображения, получаем список непустых прямоугольников
    rects = pg.mask.from_surface(img).get_bounding_rects()
    if rects:
        # мы не предполагаем, что в файле несколько отдельных картинок,
        # поэтому берём всегда первую из списка
        rect = rects[0]
        # пустая картинка нужных размеров, ПРОЗРАЧНАЯ
        cropped = pg.Surface([rect.width, rect.height], pg.SRCALPHA)
        # рисуем на созданной пустой заготовке кусок (rect) из переданной картинки
        cropped.blit(img, (0, 0), rect)
    else:
        cropped = pg.Surface(1, 1)
        rect = cropped.get_rect()
    # дальше меняем масштаб (size - это число процентов):
    width = round(rect.width * size / 100)
    height = round(rect.height * size / 100)
    return pg.transform.scale(cropped, (width, height))


def repeat_img(image, times):
    """повторяет одну и ту же картинку по горизонтали, возвращает картинку,
    составленную из них всех
    """
    pass


def append_img(image1, image2):
    """соединяет две картинки по горизонтали (используя высоту первой)"""
    pass


def append_img3(image1, image2, image3, n):
    """соединяет три картинки по горизонтали, повторяя среднюю n раз"""
    pass
