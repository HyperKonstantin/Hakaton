from config import *

class Base_Corpus:
    def __init__(self, player, corpus_img, tables_x):
        self.img = corpus_img
        self.rect = self.img.get_rect()
        self.x, self.y =  0, HEIGHT - self.rect.height
        self.player = player
        self.backdoor = pg.Rect(480, 620, 150, 200)
        self.quit = False
        self.lift_img = lift_img
        self.lift_rect = self.lift_img.get_rect()
        self.in_lift = False
        self.lift_counter = LIFT_CONST
        self.lift_moving = None # up - True, down - False, nothing - None
        self.lift_y = 0
        self.floor = 0
        self.tables_x = tables_x



    def draw(self, display : pg.Surface):
        display.blit(self.img, (self.x, self.y))

    def update(self, actions):
        self.move(actions)
        self.collider()


    def move(self, actions):
        if self.in_lift and (actions["jump"] or actions["sit"]) and self.lift_moving == None:
            if actions["jump"] and self.floor < MAX_FLOOR:
                self.lift_moving = True
                self.floor += 1
            elif actions["sit"] and self.floor > 0:
                self.lift_moving = False
                self.floor -= 1

        elif self.player.in_x_center:
            if actions["right"] and not self.is_right_border():
                self.x -= SPEED
                self.move_rects([self.backdoor], -SPEED)
                self.player.move(actions, True)
                self.player.reverse = False
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.move_rects([self.backdoor], SPEED)
                self.player.move(actions, True)
                self.player.reverse = True
            if not (actions["right"] and not self.is_right_border()) and not (actions["left"] and not self.is_left_border()):
                self.player.move(actions)
        elif self.lift_moving == None:
            self.player.move(actions)

        if actions["space"]:
            actions["space"] = False
            self.space_action()

        if self.lift_moving != None:
            self.move_lift(actions)

    def move_lift(self, actions):
        if self.lift_counter > 0:
            delta = self.lift_rect.height / LIFT_CONST
            if self.lift_moving:
                if self.is_up_border():
                    self.player.y -= delta
                    self.player.rect.y -= delta
                    self.lift_rect.y -= delta
                else:
                    self.y += delta
                self.lift_y += delta
            else:
                if self.player.rect.y < FLOOR_COORD:
                    self.player.y += delta
                    self.player.rect.y += delta
                    self.lift_rect.y += delta
                else:
                    self.y -= delta
                self.lift_y -= delta
            self.lift_counter -= 1

        else:
            self.lift_moving = None
            self.lift_counter = LIFT_CONST




    def move_rects(self, rects, x, y=0):
        for rect in rects:
            rect.x += x
            rect.y += y

    def space_action(self):
        if self.player.rect.colliderect(self.backdoor) and self.floor == 0:
            print("go to street")
            self.quit = True

        if self.player.rect.centerx in [i for  i in range(self.tables_x - 50, self.tables_x + 50)]:
            if self.num == table_corpus and self.floor == table_floor:
                self.player.text_cloud.blit("Нашёл!")

    def collider(self):
        # print(f"{self.lift_rect.y}, {self.player.rect.y}")
        if self.lift_rect.contains(self.player.rect):
            self.in_lift = True
        else:
            self.in_lift = False


    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False

    def is_up_border(self):
        return True if self.y >= 0 else False

    def is_down_border(self):
        return True if self.y <= HEIGHT - self.rect.height else False
