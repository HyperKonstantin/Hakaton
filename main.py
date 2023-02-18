
from config import *
from Scene import Scene

from button import Button

pg.init()


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



scene = Scene()
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN and event.key in player_buttons.keys():
            scene.actions[player_buttons[event.key]] = True
        elif event.type == pg.KEYUP and event.key in player_buttons.keys():
            scene.actions[player_buttons[event.key]] = False


    display.fill((100, 200, 100))
    scene.update()
    scene.draw(display)
    pg.display.flip()
    clock.tick(FPS)