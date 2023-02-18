from config import *

class Base_Corpus:
    def __init__(self, player, corpus_img):
        self.img = corpus_img
        self.rect = self.img.get_rect()
        self.x, self.y =  0, HEIGHT - self.rect.height
        self.player = player
        self.backdoor = pg.Rect(480, 620, 150, 200)
        self.quit = False

    def draw(self, display : pg.Surface):
        display.blit(self.img, (self.x, self.y))

    def update(self, actions):
        self.move(actions)

        # print(f"{self.backdoor.x}\t{self.player.rect.x}")

    def move(self, actions):
        if self.player.in_x_center :
            if actions["right"] and not self.is_right_border():
                self.x -= SPEED
                self.move_rects([self.backdoor], -SPEED)
                self.player.move(actions, True)
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.move_rects([self.backdoor], SPEED)
                self.player.move(actions, True)
            if not (actions["right"] and not self.is_right_border()) and not (actions["left"] and not self.is_left_border()):
                self.player.move(actions)
        else:
            self.player.move(actions)

        if actions["space"]:
            self.space_action()

    def move_rects(self, rects, x, y=0):
        for rect in rects:
            rect.x += x
            rect.y += y

    def space_action(self):
        if self.player.rect.colliderect(self.backdoor):
            print("go to street")
            self.quit = True



    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False

    def is_down_border(self):
        return True if self.y >= 0 else False

    def is_up_border(self):
        return True if self.y <= HEIGHT - self.rect.height else False
