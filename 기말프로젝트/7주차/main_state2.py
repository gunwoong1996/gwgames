from pico2d import *
import gfw
import player2  # 플레이어 및 여러 이미지처리
import generator2  # 동작처리
import howtostage2  # 스테이지2설명

from background import HorzScrollBackground

import gobj

canvas_width = 1000
canvas_height = 700


STATE_IN_GAME, STATE_GAME_OVER = range(2)


# 충돌체크########################
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    return distance_sq < radius_sum ** 2


def check_collision():
    global state,CRUSHOFF

###############################


# 게임시작,끝########################
def start_game():
    global state,CLEAR
    if state != STATE_GAME_OVER:
        return

    player2.reset()

    state = STATE_IN_GAME

    global score
    score = 0

    music_bg.repeat_play()

def end_game():
    global state,CHECK
    CHECK=False
    state = STATE_GAME_OVER
    music_bg.stop()

def clearstage():#스테이지클리어
    global state1

    music_bg.stop()

#######################################


# 음악삭제#############
def exit():
    global music_bg, wav_item, explosionsound,getitemsound
    del music_bg
    del explosionsound
    del wav_item
    del getitemsound


############################

# 엔터 드로우 업데이트##################### - 이곳에 반드시추가
def enter():
    gfw.world.init(['bg','bg2' ,  'player2', 'ui','redozone'])
    player2.init()
    gfw.world.add(gfw.layer.player2, player2)
    global game_over_image  # 게임오버시
    game_over_image = gfw.image.load('res/game_over.png')

    global stage1clear #스테이지1클리어시
    stage1clear=gfw.image.load('res/stage1clear.png')

    global font  # 폰트
    font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

    global music_bg, wav_item, explosionsound,getitemsound  # 음악처리
    music_bg = load_music('res/background.mp3')  # 배경음만mp3
    wav_item = load_wav('res/getitem.wav')
    explosionsound = load_wav('res/explosion.wav')
    getitemsound=load_wav('res/item.wav')

    global state
    state = STATE_GAME_OVER  # 드로우에서 처리
    start_game()  # 게임시작상태


    bg =HorzScrollBackground('space.png')
    bg.speed = 100
    gfw.world.add(gfw.layer.bg, bg)

    bg = HorzScrollBackground('spacedust.png')
    bg.speed = 150
    gfw.world.add(gfw.layer.bg2, bg)


def update():
    if state != STATE_IN_GAME:
        return
    global score
    score += gfw.delta_time
    gfw.world.update()
    generator2.update(score)
    check_collision()

def draw():
    gfw.world.draw()

    if state == STATE_GAME_OVER:
        game_over_image.draw(get_canvas_width() //2, get_canvas_height()//2)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:#엔터 게임시작
            start_game()
        elif e.key == SDLK_SPACE:#스페이스바 다음스테이지
            gfw.push(howtostage2)

    player2.handle_event(e)

def pause():
    pass

if __name__ == '__main__':
    gfw.run_main()
