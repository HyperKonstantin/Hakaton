from config import *
from corpuses.Base_Corpus import Base_Corpus
from NPC import NPC


class Corpus2(Base_Corpus):
    def __init__(self, player, corpus_img):
        super().__init__(player, corpus_img, 980)
        self.num = 2
        self.lift_rect.x, self.lift_rect.y = 1250, 600
        self.npc_count = randint(8, 8)
        npc_points = sample(corpus2_npc_collide_points, self.npc_count)
        npc_imgs = sample(npc_img_list, self.npc_count)
        self.NPCs = [NPC(npc_points[i], npc_imgs[i]) for i in range(self.npc_count)]


    def draw(self, display : pg.Surface):
        super().draw(display)
        display.blit(pg.transform.flip(self.lift_img, True, False), (self.rect.width + self.x - self.lift_rect.width - 1, self.y + 1256 - self.lift_y))


