# 스테이지2배경효과

from pico2d import *
import gfw
import player

canvas_width = 1000
canvas_height = 800

def enter():
    global image
    image = gfw.image.load('res/space1.png')

def draw():
    image.draw(500,400)


def exit():
    pass

def update():
    pass

def pause():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        pass

if __name__ == '__main__':
    gfw.run_main()