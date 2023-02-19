from config import *

class TextCloud:
    def __init__(self):
        self.img = text_cloud_img
        self.rect = self.img.get_rect()
        self.time_counter = 0
        self.is_blit = False

    def update(self, display):
        if self.is_blit and self.time_counter > 0:
            self.time_counter -= 1
            self.draw(display)
        if self.time_counter == 0:
            self.is_blit = False

    def set_coords(self, coords):
        self.coords = coords[0] - 30, coords[1] - self.rect.height + 30

    def blit(self, text):
        self.text = text
        self.is_blit = True
        self.time_counter = TEXT_TIME

    def draw(self, display : pg.Surface):

        text = cloud_font.render(self.text, False, (0, 0, 0))
        display.blit(self.img, self.coords)
        display.blit(text, (self.coords[0] + 50, self.coords[1] + 30))

