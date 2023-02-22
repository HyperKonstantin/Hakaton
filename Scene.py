from config import *
from Player import Player
from corpuses.Corpus1 import Corpus1
from corpuses.Corpus2 import Corpus2
from corpuses.Corpus3 import Corpus3

class Scene:
    def __init__(self):
        self.street_img = bg_street
        self.rect = self.street_img.get_rect()
        self.x, self.y = (0, 0)
        self.player = Player()
        self.actions = {"left": False, "right": False, "jump": False, "sit": False, "space": False}
        self.corpus = None
        self.door_rects = [pg.Rect(1100, 620, 600, 200), pg.Rect(6600, 620, 600, 200), pg.Rect(12200, 620, 600, 200)]


    def update(self, display):
        if self.corpus == None:
            self.move(self.actions)
        elif self.corpus.quit:
            self.move(self.actions)
            self.corpus = None
            self.player.x = CENTER[0]
            self.player.rect.x = CENTER[0]
            self.player.in_x_center = True
        else:
            self.corpus.update(self.actions)
        self.draw(display)

    def draw(self, display : pg.Surface):
        if self.corpus == None:
            display.blit(self.street_img, (self.x, self.y))
        else:
            self.corpus.draw(display)
        self.player.draw(display)


    def move(self, actions):
        if self.player.in_x_center :
            if actions["right"] and not self.is_right_border():
                self.x -= SPEED
                self.move_rects(-SPEED)
                self.player.reverse = False
                self.player.move(actions, True)
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.move_rects(SPEED)
                self.player.move(actions, True)
                self.player.reverse = True
            if not (actions["right"] and not self.is_right_border()) and not (actions["left"] and not self.is_left_border()):
                self.player.move(actions)
        else:
            self.player.move(actions)

        if actions["space"]:
            actions["space"] = False
            active_door = self.player.street_collides(self.door_rects)
            door_sound.play()
            match active_door:
                case 0:
                    self.corpus = Corpus1(self.player, corpus1_img)
                case 1:
                    self.corpus = Corpus2(self.player, corpus2_img)
                case 2:
                    self.corpus = Corpus3(self.player, corpus3_img)


    def move_rects(self, x, y=0):
        for rect in self.door_rects:
            rect.x += x
            rect.y += y

    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False
