import pygame as pg

from button import Button

pg.init()
SET = WIDTH, HEIGHT = 800, 500
display = pg.display.set_mode(SET)


but = Button(pg.image.load("images/btn_start.png"), pg.image.load("images/btn_start_active.png"), lambda: print("Pressed"), 2)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    display.fill((100, 200, 100))
    but.draw(display, (100, 100))
    pg.display.flip()