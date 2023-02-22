from config import *
from Scene import Scene

display = pg.display.set_mode(SET, pg.FULLSCREEN)
display.set_alpha(0)

in_menu = True
pg.mixer.music.play(-1)
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN and event.key in player_buttons.keys() and not in_menu:
            scene.actions[player_buttons[event.key]] = True
        elif event.type == pg.KEYUP and event.key in player_buttons.keys() and not in_menu:
            scene.actions[player_buttons[event.key]] = False

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and in_menu:
            in_menu = False
            scene = Scene()


    display.fill((0, 255, 0))
    if in_menu:
        display.blit(menu_img, (0, 0))
    else:
        scene.update(display)
    pg.display.flip()
    print(clock.get_fps())
    clock.tick(FPS)