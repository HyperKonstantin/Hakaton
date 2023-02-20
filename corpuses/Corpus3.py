from config import *
from corpuses.Base_Corpus import Base_Corpus

class Corpus3(Base_Corpus):
    def __init__(self, player, corpus_img):
        super().__init__(player, corpus_img, 980)
        self.num = 3
        self.lift_rect.x, self.lift_rect.y = 1250, 600
        self.npc_count = randint(2, 5)
        self.npc_points = sample(corpus1_npc_collide_points, self.npc_count)
        self.npc_imgs = sample(npc_img_list, self.npc_count)

    def draw(self, display : pg.Surface):
        super().draw(display)
        display.blit(pg.transform.flip(self.lift_img, True, False), (self.rect.width + self.x - self.lift_rect.width - 1, self.y + 1216 - self.lift_y))