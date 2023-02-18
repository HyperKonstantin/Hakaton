from config import *
from Player import Player
class Scene:
    def __init__(self):
        self.street_img = bg_street
        self.rect = self.street_img.get_rect()
        self.x, self.y = (0, 0)
        self.player = Player()
        self.actions = {"left": False, "right": False, "jump": False}

    def update(self):
        self.move(self.actions)


    def draw(self, display : pg.Surface):
        display.blit(self.street_img, (self.x, self.y))
        self.player.draw(display)

    def move(self, actions):
        if self.player.in_center :
            if actions["right"] and not self.is_right_border():
                self.x -= SPEED
                self.player.move(actions, True)
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.player.move(actions, True)
            if not (actions["right"] and not self.is_right_border()) and not (actions["left"] and not self.is_left_border()):
                print("player")
                self.player.move(actions)
        else:
            self.player.move(actions)

    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False
