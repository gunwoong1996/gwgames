import gfw
from pico2d import *
from gobj import *
from player import Player
from background import FixedBackground


canvas_width = 1000
canvas_height = 800

def enter():
    gfw.world.init(['bg', 'enemy', 'player'])

    center = get_canvas_width()//2 , get_canvas_height()//2
    bg = FixedBackground('space.png')
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.pos = bg.center
    player.bg = bg
    bg.target = player
    gfw.world.add(gfw.layer.player, player)


def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()
