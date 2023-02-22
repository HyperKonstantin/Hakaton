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
        self.exam_room_point = exam_room_point

    def draw(self, display : pg.Surface):
        # self.draw_door_collide_points()
        display.blit(self.img, (self.x, self.y))
        for npc in self.NPCs:
            npc.draw(display)

    def draw_door_collide_points(self):
        pg.draw.rect(self.img, (0, 0, 200), (1060, 520, 20, 20))
        pg.draw.rect(self.img, (0, 0, 200), (1795, 520, 20, 20))
        pg.draw.rect(self.img, (0, 0, 200), (2473, 520, 20, 20))

        pg.draw.rect(self.img, (0, 0, 200), (1060, 840, 20, 20))
        pg.draw.rect(self.img, (0, 0, 200), (1795, 840, 20, 20))
        pg.draw.rect(self.img, (0, 0, 200), (2473, 840, 20, 20))

        pg.draw.rect(self.img, (0, 0, 200), (1060, 1160, 20, 20))
        pg.draw.rect(self.img, (0, 0, 200), (1795, 1160, 20, 20))
        pg.draw.rect(self.img, (0, 0, 200), (2473, 1160, 20, 20))


    def update(self, actions):
        self.move(actions)
        self.collider()


    def move(self, actions):
        if self.in_lift and (actions["jump"] or actions["sit"]) and self.lift_moving == None and not self.player.in_jump:
            if actions["jump"] and self.floor < MAX_FLOOR:
                self.lift_moving = True
                self.floor += 1
                # lift_sound.play()
            elif actions["sit"] and self.floor > 0:
                self.lift_moving = False
                self.floor -= 1
                # lift_sound.play()

        elif self.player.in_x_center:
            if actions["right"] and not self.is_right_border():
                self.x -= SPEED
                self.exam_room_point[0] -= SPEED
                self.move_npc(-SPEED, 0)
                self.move_rects([self.backdoor], -SPEED)
                self.player.move(actions, True)
                self.player.reverse = False
            if actions["left"] and not self.is_left_border():
                self.x += SPEED
                self.exam_room_point[0] += SPEED
                self.move_npc(SPEED, 0)
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
                    self.exam_room_point[1] += delta
                    self.move_npc(0, delta)
                self.lift_y += delta
            else:
                if self.player.rect.y < FLOOR_COORD:
                    self.player.y += delta
                    self.player.rect.y += delta
                    self.lift_rect.y += delta
                else:
                    self.y -= delta
                    self.exam_room_point[1] -= delta
                    self.move_npc(0, -delta)
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
            door_sound.play()
            self.quit = True

        elif self.player.rect.centerx in [i for  i in range(self.tables_x - 120, self.tables_x + 120)]:
            if self.num == table_corpus and self.floor == table_floor:
                self.player.text_cloud.blit(table_text)

        elif self.player.rect.collidepoint(self.exam_room_point) and self.num == exam_corpus:
            door_sound.play()
            print("on exam")
            self.player.rezult()


        elif self.player.active_NPC:
            if self.player.active_NPC.is_right:
                self.player.info_counter += 1
            elif self.player.info_counter > 0:
                self.player.info_counter -= 1
            self.player.text_cloud.remove()
            self.player.active_NPC.is_asked = True
            self.player.active_NPC = None

            self.player.music_player.play()
            print(f"info: {self.player.info_counter}")

        else:
            for npc in self.NPCs:
                if not npc.is_asked and self.player.rect.collidepoint(npc.coords):
                    print("Talk with NPC")
                    self.player.active_NPC = npc
                    self.player.text_cloud.blit(npc.text, True)

                    self.player.music_player.pause()
                    self.player.music_player.mind_sound.play(-1)
                    break

    def collider(self):
        # print(f"{self.lift_rect.y}, {self.player.rect.y}")
        if self.lift_rect.contains(self.player.rect):
            self.in_lift = True
        else:
            self.in_lift = False

        if self.player.active_NPC and not self.player.rect.collidepoint(self.player.active_NPC.coords):
            self.player.active_NPC.is_asked = True
            self.player.active_NPC = None
            self.player.text_cloud.remove()
            self.player.music_player.play()




    def move_npc(self, x, y):
        for npc in self.NPCs:
            npc.move(x, y)


    def is_left_border(self):
        return True if self.x >= 0 else False

    def is_right_border(self):
        return True if self.x <= WIDTH - self.rect.width else False

    def is_up_border(self):
        return True if self.y >= 0 else False

    def is_down_border(self):
        return True if self.y <= HEIGHT - self.rect.height else False
