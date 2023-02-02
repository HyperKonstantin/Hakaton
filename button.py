from pygame import transform, mouse

# размеры изображений нажатой и не нажатой кнопок должны быть одинаковыми
class Button:
    def __init__(self, passive_img, active_img, callback, scale = 1):
        width = passive_img.get_width()
        height = passive_img.get_height()
        self.pass_img = transform.scale(passive_img, (int(width * scale), int(height * scale)))
        self.act_img = transform.scale(active_img, (int(width * scale), int(height * scale)))
        self.rect = self.pass_img.get_rect()
        self.callback = callback
        self.clicked = False

    def draw(self, surface, pos) -> None :
        self.rect.topleft = pos
        if self.rect.collidepoint(mouse.get_pos()):
            surface.blit(self.act_img, pos)
            if mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.callback()
            elif mouse.get_pressed()[0] == 0 and  self.clicked:
                self.clicked = False
        else:
            surface.blit(self.pass_img, pos)




