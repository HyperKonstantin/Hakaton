import pygame as pg

# загрузка звуков
pg.mixer.init(44100, -16, 2, 4096)
pg.mixer.music.load("sounds/MORGENSHTERN_-_POSOSI_69827135.mp3")
sound = pg.mixer.Sound("sounds/spank.wav")

# загрузка изображений
bg_street = pg.Surface((2000, 300)).fill((30, 200, 30))
player_img = pg.Surface((100, 100)).fill((200, 20, 20))

btn_start = pg.image.load("images/btn_start.png")
btn_start_active = pg.image.load("images/btn_start_active.png")

# вспомогателные структуры
player_buttons = {"jump": 119, "left": 97, "right": 100, "space": 32}