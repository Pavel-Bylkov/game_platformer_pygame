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
        cropped = pg.Surface((1, 1))
        rect = cropped.get_rect()
    # дальше меняем масштаб (size - это число процентов):
    width = round(rect.width * size / 100)
    height = round(rect.height * size / 100)
    return pg.transform.scale(cropped, (width, height))


def repeat_img(image, times=1):
    """повторяет одну и ту же картинку по горизонтали, возвращает картинку,
    составленную из них всех
    """
    if times > 0:
        rect = image.get_rect()
        w = rect.width
        img = pg.Surface((w * times, rect.height), pg.SRCALPHA)
        for i in range(times):
            img.blit(image, (w * i, 0))
        return img
    return pg.Surface((1, 1))


def append_img(image1, image2):
    """соединяет две картинки по горизонтали (используя высоту первой)"""
    rect1 = image1.get_rect()
    rect2 = image2.get_rect()
    w = rect1.width + rect2.width
    img = pg.Surface([w, rect1.height], pg.SRCALPHA)
    img.blit(image1, (0, 0))
    img.blit(image2, (rect1.width, 0))
    return img


def append_img3(image1, image2, image3, n):
    """соединяет три картинки по горизонтали, повторяя среднюю n раз"""
    img_l = image1
    if n > 0:
        img_l = append_img(img_l, repeat_img(image2, n))
    img = append_img(img_l, image3)
    return img
