
from config import *
from Scene import Scene

from button import Button

pg.init()


display = pg.display.set_mode(SET, pg.FULLSCREEN)

pg.mixer.music.play(-1)

music = False
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
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
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
    # print(clock.get_fps())
    clock.tick(FPS)