from config import *
from corpuses.Base_Corpus import Base_Corpus
from NPC import NPC


class Corpus1(Base_Corpus):
    def __init__(self, player, corpus_img):
        super().__init__(player, corpus_img, 545)
        self.num = 1
        self.lift_rect.x, self.lift_rect.y = 0, 600
        self.npc_count = randint(8, 8)
        npc_points = sample(corpus1_npc_collide_points, self.npc_count)
        npc_imgs = sample(npc_img_list, self.npc_count)
        self.NPCs = [NPC(npc_points[i], npc_imgs[i]) for i in range(self.npc_count)]

    def draw(self, display : pg.Surface):
        super().draw(display)
        display.blit(self.lift_img, (self.x + 1, self.y + 1236 - self.lift_y))


        # print(f"{self.exam_room_point}, ({self.player.rect.centerx}, {self.player.rect.centery})")
