from config import *

class NPC:
    def __init__(self, coords, img):
        self.coords = coords
        self.img = img
        self.is_right = randint(1, 2) < 2
        self.is_asked = False
        if self.is_right:
            self.text = choice(exam_phrases[exam_subject])
        else:
            self.text = choice(exam_phrases[choice(list(filter(lambda x: x != exam_subject,subjects)))])

    def draw(self, display):
        display.blit(self.img, (self.coords[0] - 75, self.coords[1] - 75))

    def move(self, x, y):
        self.coords[0] += x
        self.coords[1] += y

    def change_exam_room(self, old_exam_room):
        global exam_room, exam_floor, exam_corpus, exam_room_point, table_text
        exam_corpus = randint(1, 1)
        exam_floor = randint(1, 3)
        exam_room = randint(1, 3)

        d_x, d_y = exam_room_point[0] - old_exam_room[0], exam_room_point[1] - old_exam_room[1]

        exam_room_point = [corpuses_door_collide_points[exam_corpus - 1][0][exam_room - 1] - d_x,
                       corpuses_door_collide_points[exam_corpus - 1][1][exam_floor - 1] - d_y]

        table_text = f"Вот оно! Оказывается у\nменя экзамен по {exam_subject}\nв {exam_corpus}-{exam_floor + 1}0{exam_room} кабинете.\nГлавное - не забыть!"
        print(f"exam room: {exam_corpus}-{exam_floor + 1}0{exam_room}")
        return exam_room_point
