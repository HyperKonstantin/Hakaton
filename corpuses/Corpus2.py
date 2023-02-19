from config import *
from corpuses.Base_Corpus import Base_Corpus

class Corpus2(Base_Corpus):
    def __init__(self, player, corpus_img):
        super().__init__(player, corpus_img)
        self.lift_rect.x, self.lift_rect.y = 1250, 600

    def draw(self, display : pg.Surface):
        super().draw(display)
        display.blit(pg.transform.flip(self.lift_img, True, False), (self.rect.width + self.x - self.lift_rect.width, self.y + 916 - self.lift_y))


