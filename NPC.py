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