from config import *

class Corpus1:
    def __init__(self, player):
        self.img = corpus1_img
        self.rect = self.img.get_rect()
        self.x, self.y = HEIGHT - self.rect.height, self.rect.width // 2
        self.player = player

    def draw(self, display : pg.Surface):
        display.blit(self.img, (self.x, self.y))

    def update(self, actions):
        self.move(actions)

    def move(self, actions):
        if self.player.in_x_center :
            if actions["right"] and not self.is_right_border():
                self.x -= SPEED
                self.player.move(actions, True)
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.player.move(actions, True)
            if not (actions["right"] and not self.is_right_border()) and not (actions["left"] and not self.is_left_border()):
                self.player.move(actions)
        else:
            self.player.move(actions)

    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False

    def is_down_border(self):
        return True if self.y >= 0 else False

    def is_up_border(self):
        return True if self.y <= HEIGHT - self.rect.height else False