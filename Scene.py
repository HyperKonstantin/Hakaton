from config import *
from Player import Player
from corpuses.Corpus1 import Corpus1
from corpuses.Corpus2 import Corpus2
from corpuses.Corpus3 import Corpus3
from TextCloud import TextCloud

class Scene:
    def __init__(self):
        self.street_img = bg_street
        self.rect = self.street_img.get_rect()
        self.x, self.y = (0, 0)
        self.player = Player()
        self.actions = {"left": False, "right": False, "jump": False, "sit": False, "space": False}
        self.corpus = None
        self.door_rects = [pg.Rect(1100, 620, 600, 200), pg.Rect(6600, 620, 600, 200), pg.Rect(12200, 620, 600, 200)]
        self.corpus_cache = {1: None, 2: None, 3: None}
        self.last_corpus = None
        self.help_npc_coords = (430, 750)
        self.help_npc_counter = 0
        self.text_cloud = TextCloud([500, 500])


    def update(self, display):
        if self.corpus == None:
            self.move(self.actions)
        elif self.corpus.quit:
            self.move(self.actions)
            self.corpus.quit = False
            self.last_corpus = self.corpus
            self.corpus_cache[self.corpus.num] = self.corpus
            if all(self.corpus_cache.values()):
                print("all")
                self.corpus_cache = {1: None, 2: None, 3: None}
            self.corpus = None
            self.player.x = CENTER[0]
            self.player.rect.x = CENTER[0]
            self.player.in_x_center = True
        else:
            self.corpus.update(self.actions)
        self.draw(display)
        self.text_cloud.update(display)

        # print(f"{self.corpus_cache}")

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
                self.text_cloud.change_coords(-SPEED)
                self.move_rects(-SPEED)
                self.player.reverse = False
                self.player.move(actions, True)
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.text_cloud.change_coords(SPEED)
                self.move_rects(SPEED)
                self.player.move(actions, True)
                self.player.reverse = True
            if not (actions["right"] and not self.is_right_border()) and not (actions["left"] and not self.is_left_border()):
                self.player.move(actions)
        else:
            self.player.move(actions)

        if actions["space"]:
            actions["space"] = False
            if self.player.rect.collidepoint(self.help_npc_coords):
                if self.help_npc_counter < 4:
                    self.text_cloud.blit(help_messages_list[self.help_npc_counter])
                    self.help_npc_counter += 1
                return
            active_door = self.player.street_collides(self.door_rects)
            if active_door != -1:
                self.text_cloud.remove()
                print(f"{self.last_corpus=}")
            match active_door:
                case 0:
                    if self.last_corpus != None and self.last_corpus.num == 1:
                        self.corpus = self.last_corpus
                    else:
                        if self.corpus_cache[1] == None:
                            self.corpus = Corpus1(self.player, corpus1_img)
                        else:
                            self.corpus = self.corpus_cache[1]

                case 1:
                    if self.last_corpus != None and self.last_corpus.num == 2:
                        self.corpus = self.last_corpus
                    else:
                        if self.corpus_cache[2] == None:
                            self.corpus = Corpus2(self.player, corpus2_img)
                        else:
                            self.corpus = self.corpus_cache[2]

                case 2:
                    if self.last_corpus != None and self.last_corpus.num == 3:
                        self.corpus = self.last_corpus
                    else:
                        if self.corpus_cache[3] == None:
                            self.corpus = Corpus3(self.player, corpus3_img)
                        else:
                            self.corpus = self.corpus_cache[3]

    def move_rects(self, x, y=0):
        for rect in self.door_rects:
            rect.x += x
            rect.y += y

    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False
