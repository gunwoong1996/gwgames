# 스테이지2배경효과

from pico2d import *
import gfw
import player
import main_state2

canvas_width = 1000
canvas_height = 700

def enter():
    global image
    image = gfw.image.load('res/game_over.png')

def draw():
    image.draw(500,350)

def exit():
    #del music_bg
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
    elif e.key == SDLK_RETURN:  # 엔터 게임시작
        gfw.push(main_state2)


if __name__ == '__main__':
    gfw.run_main()