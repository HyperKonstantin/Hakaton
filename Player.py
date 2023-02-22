from config import *
from TextCloud import TextCloud
from End_game import End_game
from Music_Player import Music_player
class Player:
    def __init__(self):
        self.player_stand_img = player_img
        self.right_animation_imgs = [player_stand_right_img, player_goes_right_img]
        self.left_animation_imgs = [player_stand_left_img, player_goes_left_img]
        self.rect = self.player_stand_img.get_rect()
        self.reverse = False
        self.moving = False
        self.in_x_center = True
        self.jump_counter = JUMP_CONST
        self.animation_counter = 0
        self.in_jump = False
        self.x, self.y = (CENTER[0], 670)
        self.rect.x, self.rect.y = (CENTER[0], 670)
        self.text_cloud = TextCloud()
        self.active_NPC = False
        self.info_counter = 0
        self.end_game = End_game()
        self.bell_counter = 1
        self.music_player = Music_player()
        self.is_end = False
        self.start_time = time()

    def move(self, actions, block_move=False):
        if not block_move:
            if actions["right"] and self.x < WIDTH - self.rect.width - SPEED:
                self.x += SPEED
                self.move_rect(self.rect, SPEED)
                self.reverse = False
            if actions["left"] and self.x > SPEED:
                self.x -= SPEED
                self.move_rect(self.rect, -SPEED)
                self.reverse = True
        if actions["jump"]:
            self.in_jump = True
        if self.in_jump:
            self.jump()

        if not actions["right"] and not actions["left"]:
            self.moving = False
        else:
            self.moving = True

        self.in_x_center = True if self.x == CENTER[0] else False

    def move_rect(self, rect, x, y=0):
            rect.x += x
            rect.y += y

    def jump(self):
        if self.jump_counter > 0:
            self.y -= (self.jump_counter ** 2)
            self.rect.y -= (self.jump_counter ** 2)
        if self.jump_counter < 0:
            self.y += (self.jump_counter ** 2)
            self.rect.y += (self.jump_counter ** 2)
        if self.jump_counter == -JUMP_CONST:
            self.jump_counter = JUMP_CONST
            self.in_jump = False
            # self.y = FLOOR_COORD
            # self.rect.y = FLOOR_COORD
            return
        self.jump_counter -= 1

    def animation(self):
        self.animation_counter += 1
        if self.animation_counter >= ANIMATION_CONST:
            self.animation_counter = 0

        return self.right_animation_imgs[self.animation_counter // (ANIMATION_CONST // 2)]

    def draw(self, display : pg.Surface):
        img = self.animation() if self.moving else self.player_stand_img
        img = pg.transform.flip(img, True, False) if self.reverse else img
        display.blit(img, (self.x, self.y))

        #text
        self.text_cloud.set_coords(self.rect.topright)
        self.text_cloud.update(display)

        #end game
        self.end_game.check(display, self.music_player)

        self.bell_update()


    def street_collides(self, doors):
        for i, door in enumerate(doors):
            if self.rect.colliderect(door):
                return i
        return None

    def bell_update(self):
        now_time = time()
        if self.bell_counter > BELLS_COUNT - 1 and not self.is_end:
            self.music_player.end_music()
            self.is_end = True
        if self.bell_counter > BELLS_COUNT:
            self.end_game.set_end(is_late=True)
        elif int(now_time - self.start_time) == GAME_TIME * self.bell_counter and not  self.end_game.run_end_sound:
            bell_sound.play()
            self.bell_counter += 1

    def rezult(self):
        if self.info_counter >= randint(1, MAX_INFO_POINTS):
            self.end_game.set_end(is_pass=True)
        else:
            self.end_game.set_end(is_fail=True)