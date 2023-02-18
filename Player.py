from config import *
class Player:
    def __init__(self):
        self.img = player_img
        self.reverse = False
        self.jump_counter = 0
        self.pos = self.x, self.y = (400, 400)

    def move(self, side):
        if side == "right":
            self.x += 1
        elif side == "left":
            self.x -= 1

    def draw(self, display : pg.Surface):
        img = pg.transform.flip(self.img, True, False) if self.reverse else self.img
        display.blit(img, self.pos)


