#플레이어처리

from pico2d import *
import gfw

MOVE_PPS = 250
MAX_LIFE = 5


def init():
    global image, pos, radius,image1

    image = gfw.image.load('res/player.png')

    radius = image.h // 2

    global o2insert, o2del,o2tank
    o2insert = gfw.image.load('res/o2insert.png')
    o2del = gfw.image.load('res/o2del.png')
    o2tank =gfw.image.load('res/o2tank.png')
    reset()

def reset():
    global image, pos, radius
    pos = get_canvas_width() // 2, get_canvas_height() // 2

    global delta_x, delta_y
    delta_x, delta_y = 0, 0

    global life
    life = MAX_LIFE

def decrease_life():
    global life
    life -= 1
    return life <= 0

def update():
    global pos, delta_x, delta_y
    x, y = pos
    x += delta_x * MOVE_PPS * gfw.delta_time
    y += delta_y * MOVE_PPS * gfw.delta_time

    hw, hh = image.w // 2, image.h // 2
    x = clamp(hw, x, get_canvas_width() - hw)
    y = clamp(hh, y, get_canvas_height() - hh)
    pos = x, y

def draw():
    global image, pos
    image.draw(*pos)#플레이어
    o2tank.draw(get_canvas_width() - 30,get_canvas_height() - 680)#산소통이미지
    #산소통게이지
    x, y = get_canvas_width() - 36, get_canvas_height() - 780
    for i in range(MAX_LIFE):
        o2 = o2insert if i < life else o2del
        o2.draw(x, y)
        y+=30

def handle_event(e):
    global delta_x, delta_y
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_LEFT:
            delta_x -= 1

        elif e.key == SDLK_RIGHT:
            delta_x += 1
        elif e.key == SDLK_DOWN:
            delta_y -= 1
        elif e.key == SDLK_UP:
            delta_y += 1
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            delta_x += 1
        elif e.key == SDLK_RIGHT:
            delta_x -= 1
        elif e.key == SDLK_DOWN:
            delta_y += 1
        elif e.key == SDLK_UP:
            delta_y -= 1
