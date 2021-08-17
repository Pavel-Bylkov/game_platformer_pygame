from config.constants import *

background_win = f'{DIR_IMG}win.png'
background_fail = f'{DIR_IMG}over.jpg'

# graphic_filenames - список с информацией о картинках героев
# в нем лежат записи формата [имя картинки, масштаб (процентов)].
# Используем константы в качестве индексов, чтобы не путаться,
# в каком месте списка кто должен оказаться.
# Программа будет работать нормально при любом порядке добавления картинок, и любых значениях констант,
# если только gr_total больше любой другой.

# создает список нужной длины (в python 3 range() - это не список, надо переводить)
graphic_filenames = list(range(GR_TOTAL))

graphic_filenames[GR_HERO] = [f'{DIR_IMG}m1.png', 16]
graphic_filenames[GR_ENEMY] = [f'{DIR_IMG}st1.png', 16]
graphic_filenames[GR_PLAT_L] = [f'{DIR_IMG}plat_l.png', 30]
graphic_filenames[GR_PLAT_M] = [f'{DIR_IMG}plat.png', 30]
graphic_filenames[GR_PLAT_R] = [f'{DIR_IMG}plat_r.png', 30]
graphic_filenames[GR_FIRE] = [f'{DIR_IMG}arrow.png', 16]
graphic_filenames[GR_E_FIRE] = [f'{DIR_IMG}stone1.png', 10]
graphic_filenames[GR_ENEMY2] = [f'{DIR_IMG}varvar.png', 16]
graphic_filenames[GR_GOAL] = [f'{DIR_IMG}door.png', 20]

