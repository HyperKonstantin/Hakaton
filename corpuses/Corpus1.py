from config import *
from corpuses.Base_Corpus import Base_Corpus


class Corpus1(Base_Corpus):
    def __init__(self, player, corpus_img):
        super().__init__(player, corpus_img, 530)
        self.num = 1
        self.lift_rect.x, self.lift_rect.y = 0, 600

    def draw(self, display : pg.Surface):
        super().draw(display)
        display.blit(self.lift_img, (self.x, self.y + 916 - self.lift_y))
