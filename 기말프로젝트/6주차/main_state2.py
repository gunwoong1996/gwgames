import gfw
from pico2d import *
from player2 import Player
from stage2bg import HorzScrollBackground
import gobj
canvas_width = 1000
canvas_height = 700


def enter():
    gfw.world.init(['bg', 'player', 'bg2', 'ui'])

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

    bg = HorzScrollBackground('space.png')
    bg.speed = 50
    gfw.world.add(gfw.layer.bg, bg)

    bg = HorzScrollBackground('spacedust.png')
    bg.speed = 30
    gfw.world.add(gfw.layer.bg2, bg)


##############################################

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
