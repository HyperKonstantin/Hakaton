import pygame as pg
from random import randint, choice, sample

#TODO баг при прыжке в лифт

# Константы
SET = WIDTH, HEIGHT = 1536, 864
CENTER = WIDTH // 2, HEIGHT // 2
FPS = 100
SPEED = 30
FLOOR_COORD = 670
JUMP_CONST = 7
ANIMATION_CONST = 10
LIFT_CONST = 20
MAX_FLOOR = 3
TEXT_TIME = 100

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
lift_img = pg.image.load("images/img_lift.png")
text_cloud_img = pg.transform.flip(pg.image.load("images/img_text_cloud.png"),True, False)
npc_img_list = [pg.image.load(f"images/NPC/img_npc_{i}.png") for i in range(1, 9)]

# загрузка шрифтов sourcecodeproblack
pg.init()
font = choice(pg.font.get_fonts())
# print(font)
cloud_font = pg.font.SysFont("sourcecodeproblack", 25)

# вспомогателные структуры
player_buttons = {119: "jump", pg.K_s : "sit", 97: "left", 100: "right", 32: "space"}
subjects = ["матану", "физике", "метрологии"]

exam_phrases = {"матану": ["Фраза по матану 1", "Фраза по матану 2", "Фраза по матану 3"],
               "физике": ["Фраза по физике 1", "Фраза по физике 2", "Фраза по физике 3"],
               "метрологии": ["Фраза по метрологии 1", "Фраза по метрологии 2", "Фраза по метрологии 3"]
                }

dialog_texts = ["Фраза по матану 1", "Фраза по матану 2", "Фраза по матану 3", "Фраза по физике 1", "Фраза по физике 2", "Фраза по физике 3"]


corpuses_door_collide_points = [[(1060, 1795, 2473), (1160 - 726, 840  - 726, 520  - 726)] # 1 корпус
                                ]


corpus1_npc_collide_points = [[i + 350, j] for i in corpuses_door_collide_points[0][0] for j in corpuses_door_collide_points[0][1]]

# генерация
exam_corpus = randint(1, 1)
exam_floor = randint(1, 3)
exam_room = randint(1, 3)
exam_room_point = [corpuses_door_collide_points[exam_corpus - 1][0][exam_room - 1], corpuses_door_collide_points[exam_corpus - 1][1][exam_floor - 1]]
exam_subject = choice(subjects)

table_corpus = randint(1, 1)
table_floor = randint(1, 3)
table_text = f"Вот оно! Оказывается у\nменя экзамен по {exam_subject}\nв {exam_corpus}-{exam_floor + 1}0{exam_room} кабинете.\nГлавное - не забыть!"


print(f"table: {table_corpus}-{table_floor + 1}")
print(f"exam room: {exam_corpus}-{exam_floor + 1}0{exam_room}")