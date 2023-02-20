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

    def blit(self, text, nonestop=False):
        self.text = text
        self.is_blit = True
        self.time_counter = 100000 if nonestop else TEXT_TIME

    def remove(self):
        self.time_counter = 0

    def draw(self, display : pg.Surface):

        text = cloud_font.render(self.text, False, (0, 0, 0))
        display.blit(self.img, self.coords)
        # display.blit(text, (self.coords[0] + 30, self.coords[1] + 10))
        self.blit_text(display, self.text, (self.coords[0] + 30, self.coords[1] + 10) , cloud_font)

    def blit_text(self, surface, text, pos, font, color=pg.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = 10000, 1000
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

