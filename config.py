import pygame as pg

# загрузка звуков
pg.mixer.init(44100, -16, 2, 4096)
pg.mixer.music.load("sounds/MORGENSHTERN_-_POSOSI_69827135.mp3")
sound = pg.mixer.Sound("sounds/spank.wav")

# загрузка изображений
btn_start = pg.image.load("images/btn_start.png")
btn_start_active = pg.image.load("images/btn_start_active.png")