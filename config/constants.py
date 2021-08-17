import os

# Глобальные константы (настройки)
WIN_X = 800
WIN_Y = 600
TITLE = "ARCADA"

FPS = 60

GRAVITY = 0.15
HERO_JUMP = -7
HERO_SPEED = 5
HERO_START_LIVES = 3


C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)


DIR_IMG = 'img' + os.sep   # separate - разделитель в Windows \, а в Linux(Mac os) - /

# индексы для списка картинок
GR_HERO = 0
GR_ENEMY = 1
GR_PLAT_L = 2
GR_PLAT_M = 3
GR_PLAT_R = 4
GR_FIRE = 5
GR_E_FIRE = 6
GR_ENEMY2 = 7
GR_GOAL = 8
# общее число картинок
GR_TOTAL = 9
