# 스테이지2배경효과

from pico2d import *
import gfw
import player
import main_state2

canvas_width = 1000
canvas_height = 700

def music():
    music_bg.repeat_play()


def enter():
    global image
    image = gfw.image.load('res/stage2clear.png')

    global music_bg
    music_bg = load_music('res/titlemusic.mp3')  # 배경음만mp3

    music()

def draw():
    image.draw(500,350)
    music()


def exit():
    global music_bg
    del music_bg



def update():
    music()
    pass

def pause():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

if __name__ == '__main__':
    gfw.run_main()