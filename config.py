import pygame as pg

# Константы
SET = WIDTH, HEIGHT = 1536, 864
CENTER = WIDTH // 2, HEIGHT // 2
FPS = 100
SPEED = 24
JUMP_CONST = 10
ANIMATION_CONST = 10

# загрузка звуков
pg.mixer.init(44100, -16, 2, 4096)
pg.mixer.music.load("sounds/MORGENSHTERN_-_POSOSI_69827135.mp3")
sound = pg.mixer.Sound("sounds/spank.wav")

# загрузка изображений
bg_street = pg.image.load("images/img_street.png")
corpus1_img = pg.image.load("images/img_corpus_1.png")
corpus2_img = pg.image.load("images/img_corpus_2.png")
corpus3_img = pg.image.load("images/img_corpus_3.png")
player_img = pg.image.load("images/img_player.png")
player_stand_right_img = pg.image.load("images/img_player_stand_right.png")
player_goes_right_img = pg.image.load("images/img_player_goes_right.png")
player_stand_left_img = pg.image.load("images/img_player_stand_left.png")
player_goes_left_img = pg.image.load("images/img_player_goes_left.png")

btn_start = pg.image.load("images/btn_start.png")
btn_start_active = pg.image.load("images/btn_start_active.png")

# вспомогателные структуры
player_buttons = {119: "jump", 97: "left", 100: "right", 32: "space"}