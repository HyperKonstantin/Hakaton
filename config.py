import pygame as pg

# Константы
SET = WIDTH, HEIGHT = 1536, 864
CENTER = WIDTH // 2, HEIGHT // 2
FPS = 80
SPEED = 6
JUMP_CONST = 20

# загрузка звуков
pg.mixer.init(44100, -16, 2, 4096)
pg.mixer.music.load("sounds/MORGENSHTERN_-_POSOSI_69827135.mp3")
sound = pg.mixer.Sound("sounds/spank.wav")

# загрузка изображений
# bg_street = pg.Surface((2000, 300)).fill((30, 200, 30))
bg_street = pg.image.load("images/img_street.png")
# player_img = pg.Surface((100, 100)).fill((200, 20, 20))
player_img = pg.image.load("images/img_player.png")

btn_start = pg.image.load("images/btn_start.png")
btn_start_active = pg.image.load("images/btn_start_active.png")

# вспомогателные структуры
player_buttons = {119: "jump", 97: "left", 100: "right", 32: "space"}