from config import *

class End_game:
    def __init__(self):
        self.is_pass = False
        self.pass_img = pass_img
        self.is_fail = False
        self.fail_img = fail_img
        self.is_late = False
        self.late_img = late_img
        self.alpha_counter = 0
        self.black_screen = pg.Surface(SET)
        self.run_end_sound = False

        self.black_screen.fill((0, 0, 0))

    def check(self, display, music_player):
        if any([self.is_pass, self.is_fail, self.is_late]):
            if self.alpha_counter >= 255:
                self.end_screen(display)
                if not self.run_end_sound:
                    self.end_music(music_player)
                    self.run_end_sound = True
            else:
                self.end_game(display)

    def end_game(self, display : pg.Surface):
        self.black_screen.set_alpha(self.alpha_counter)
        display.blit(self.black_screen, (0, 0))
        self.alpha_counter += 5

    def set_end(self, is_pass=False, is_fail=False, is_late=False):
        if is_pass and not self.is_fail and not self.is_late:
            self.is_pass = True
        if is_fail and not self.is_pass and not self.is_late:
            self.is_fail = True
        if is_late and not self.is_fail and not self.is_pass:
            self.is_late = True

    def end_screen(self, display : pg.Surface):
        if self.is_late:
            display.blit(self.late_img, (0, 0))
        if self.is_fail:
            display.blit(self.fail_img, (0, 0))
        if self.is_pass:
            display.blit(self.pass_img, (0, 0))

    def end_music(self, music_player):
        music_player.pause()
        if self.is_late:
            music_player.fail_sound.play()
            print("Late")
        if self.is_fail:
            music_player.fail_sound.play()
            print("Fail")
        if self.is_pass:
            music_player.pass_sound.play()
            print("Pass")

