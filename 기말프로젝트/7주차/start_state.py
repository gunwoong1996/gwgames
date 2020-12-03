import gfw
from pico2d import *
import howtostage1

canvas_width = 1000
canvas_height = 700

def enter():
    global image,titlemusic
    titlemusic = load_music('res/titlemusic.mp3')
    image = gfw.image.load('res/title.png')
    titlemusic.repeat_play()

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
        gfw.push(howtostage1)
def exit():
    global image,titlemusic
    del image
    del titlemusic

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()

