import time

import pygame as pg
from random import randint, choice, sample
from time import time

#TODO баг при прыжке в лифт

# Константы
SET = WIDTH, HEIGHT = 1536, 864
CENTER = WIDTH // 2, HEIGHT // 2
FPS = 20
SPEED = 50
FLOOR_COORD = 670
JUMP_CONST = 5
ANIMATION_CONST = 10
LIFT_CONST = 20
MAX_FLOOR = 3
TEXT_TIME = 100
GAME_TIME = 60
BELLS_COUNT = 10
MAX_INFO_POINTS = 5

# загрузка звуков
pg.mixer.init(44100, -16, 2, 4096)
pg.mixer.music.load("sounds/sound_fon_default.mp3")
fail_sound = pg.mixer.Sound("sounds/sound_fail.wav")
pass_sound = pg.mixer.Sound("sounds/sound_pass.wav")
mind_sound = pg.mixer.Sound("sounds/sound_mind.wav")
door_sound = pg.mixer.Sound("sounds/sound_door.mp3")


bell_sound = pg.mixer.Sound("sounds/sound_bell.mp3")

# загрузка изображений
bg_street = pg.image.load("images/img_street_cool.png")
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
pass_img = pg.image.load("images/img_pass.png")
fail_img = pg.image.load("images/img_fail.png")
late_img = pg.image.load("images/img_late.png")
menu_img = pg.image.load("images/img_menu.png")

# загрузка шрифтов sourcecodeproblack
pg.init()
font = choice(pg.font.get_fonts())
# print(font)
cloud_font = pg.font.SysFont("sourcecodeproblack", 25)

# вспомогателные структуры
player_buttons = {119: "jump", pg.K_s : "sit", 97: "left", 100: "right", 32: "space"}
subjects = ["матану", "физике", "философии"]

exam_phrases = {"матану": ["Дифференциал - это\nприращение функции.\nНужно ли мне это?",
                           "Пригодится ли мне\nформула Ньютона-\nЛейбница?",
                           "Что за Тейлор? Это\nточно мне нужно?",
                           "Говорят, мне точно\nнужно знать, кто\nтакой Коши.",
                           "Криволинейный интеграл.\nЭто что вообще такое?",
                           "Запоминать ли мне 10\nзнаков после запятой в\nчисле пи?",
                           "Мне правда нужно\nуметь раскрывать\nнеопределённости?",
                           "Комплексные числа?\nНе слышал, что такие\nесть.",
                           "Понадобится ли мне\nтаблица производных?",
                           "Пределы - это база.\nТолько помогут ли\nони мне?"],

               "физике": ["Законы термодинамики,\nнадо ли их знать?",
                          "Нужно ли знать\nфотоэффект?",
                          "Что такое электромаг-\nнитное поле?",
                          "Понадобиться ли знание\nволновой функции?",
                          "Стоит ли знать какое\nтело абсолютно черное?",
                          "Гистерезис, понадобиться\nли такое на экзамене",
                          "Что там Планк придумал,\nстоит ли такое\nзапоминать?",
                          "Так надо понимать что\nтакое дифракция или не?",
                          "Закон смещения Вина,\nи вот это мне надо\nзапоминать?",
                          "Надо или не надо эта\nваша фотопроводимость\nполупроводников"],

               "философии": ["Философия стоицизма,\nнужно ли ее знать?",
                             "Надо ли знать смысл\nтрудов Гегеля?",
                             "Метафизика, интересно\nпригодится ли?",
                             "Субъективный идеализм,\nэто вообще что",
                             "Да кто эти модернисты\nтакие",
                             "Надо ли знать про\nсверхчеловека по Ницше?",
                             "Буддизм. Интересно\nможет это мне поможет\nна экзамене",
                             "Понадобиться ли мне\nзнание о неопозитивизме",
                             "Феноменология духа,\nзвучит ли как что-то\nполезное?",
                             "Сократ, какой-то умный\nчел, надо ли его знать?" ]


                }

help_messages_list = ["Привет, у нас сегодня\nэкзамен",
                      "Только я не помню по\nкакому предмету и в\nкакой аудитории он\nбудет",
                      "Времени осталось не\nмного - так что\nбеги ищи",
                      "Поспрашивай ребят\nвокруг, чтоб как\nнибудь подготовиться"]


corpuses_door_collide_points = [[(1060, 1795, 2473), (1160 - 726, 840 - 726, 520 - 726)],  # 1 корпус
                                [(1055, 1735, 2470), (1170 - 750, 850 - 750, 530 - 750)],
                                [(1055, 1735, 2470), (1120 - 708, 790 - 708, 470 - 708)] # 2 корпус
                                ]


corpus1_npc_collide_points = [[i + randint(200, 500), j] for i in corpuses_door_collide_points[0][0] for j in corpuses_door_collide_points[0][1]]
corpus2_npc_collide_points = [[i - randint(200, 500), j] for i in corpuses_door_collide_points[1][0] for j in corpuses_door_collide_points[1][1]]
corpus3_npc_collide_points = [[i - randint(200, 500), j] for i in corpuses_door_collide_points[2][0] for j in corpuses_door_collide_points[2][1]]


# генерация
exam_corpus = randint(1, 3)
exam_floor = randint(1, 3)
exam_room = randint(1, 3)
exam_room_point = [corpuses_door_collide_points[exam_corpus - 1][0][exam_room - 1], corpuses_door_collide_points[exam_corpus - 1][1][exam_floor - 1]]
exam_subject = choice(subjects)

table_corpus = randint(1, 3)
table_floor = randint(1, 3)
table_text = f"Вот оно! Оказывается у\nменя экзамен по {exam_subject}\nв {exam_corpus}-{exam_floor + 1}0{exam_room} кабинете.\nГлавное - не забыть!"

print(f"table: {table_corpus}-{table_floor + 1}")
print(f"exam room: {exam_corpus}-{exam_floor + 1}0{exam_room}")