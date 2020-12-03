import gfw
from pico2d import *
import main_state

canvas_width = 1000
canvas_height = 700


def enter():
    global image
    image = gfw.image.load('res/howtostage1.png')

def update():
    pass


def draw():
    image.draw(500, 350)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)


def exit():
    pass

def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()

