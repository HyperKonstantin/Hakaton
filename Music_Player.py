from config import *

class Music_player:
    def __init__(self):
        self.fon_music = pg.mixer.music
        self.pass_sound = pass_sound
        self.fail_sound = fail_sound
        self.mind_sound = mind_sound

    def play(self):
        self.mind_sound.stop()
        self.fon_music.play(-1)

    def pause(self):
        self.fon_music.stop()

    def end_music(self):
        return
        pg.mixer.music.load("sounds/sound_fon_end.mp3")
        self.fon_music = pg.mixer.music
        self.fon_music.play(-1)


