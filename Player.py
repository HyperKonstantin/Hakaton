from config import *
class Player:
    def __init__(self):
        self.img = player_img
        self.reverse = False
        self.in_center = True
        self.jump_counter = JUMP_CONST
        self.in_jump = False
        self.x, self.y = (CENTER[0], 550)

    def move(self, actions, block_move=False):
        if not block_move:
            if actions["right"]:
                self.x += SPEED
            if actions["left"]:
                self.x -= SPEED
        if actions["jump"]:
            self.in_jump = True
        if self.in_jump:
            self.jump()

        self.in_center = True if self.x == CENTER[0] else False

    def jump(self):
        if self.jump_counter > 0:
            self.y -= (self.jump_counter ** 2) / 20
        if self.jump_counter < 0:
            self.y += (self.jump_counter ** 2) / 20
        if self.jump_counter == -JUMP_CONST:
            self.jump_counter = JUMP_CONST
            self.in_jump = False
            return
        self.jump_counter -= 1


    def draw(self, display : pg.Surface):
        img = pg.transform.flip(self.img, True, False) if self.reverse else self.img
        display.blit(img, (self.x, self.y))


