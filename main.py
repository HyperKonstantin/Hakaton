from config import *

from button import Button

pg.init()

SET = WIDTH, HEIGHT = 800, 500
display = pg.display.set_mode(SET)

pg.mixer.music.play(-1)

music = True
def set_music():
    global music
    music = not music

    if music:
        pg.mixer.music.unpause()
    else:
        pg.mixer.music.pause()




but = Button(btn_start, btn_start_active, set_music, 2)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                sound.play()
                print("space")

    display.fill((100, 200, 100))
    but.draw(display, (100, 100))
    pg.display.flip()