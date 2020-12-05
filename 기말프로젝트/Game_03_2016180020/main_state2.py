from pico2d import *
import gfw
import player2  # 플레이어 및 여러 이미지처리
import generator2  # 동작처리
import howtostage2  # 스테이지2설명
import restart
import ending
from background import HorzScrollBackground

import gobj

canvas_width = 1000
canvas_height = 700
CLEAR=False
CHECK=True
START=True


STATE_IN_GAME, STATE_GAME_OVER ,STATE_CLEAR= range(3)
def gdel():
    global CHECK

    CHECK=False

# 충돌체크########################
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    return distance_sq < radius_sum ** 2

def collides_distance1(a, b):#위치용
    ax, ay = a.pos1
    bx, by = b.pos1
    radius_sum = a.radius + b.radius
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    return distance_sq < radius_sum ** 2

def check_collision():#지구도착
    for a in gfw.world.objects_at(gfw.layer.arrivepoint):
        global CLEAR
        if collides_distance1(player2, a):
            gfw.world.remove((a))
            clearmusic.play()
            stageclear()

    for b in gfw.world.objects_at(gfw.layer.redozone):#레드충돌
        if collides_distance(player2, b):
            gfw.world.remove((b))
            dead = player2.decrease_life()
            wav_item.play()


            if dead:  # 게임오버
                end_game()

            player2.redshielddel()#방패제거
            player2.blueshielddel()
            player2.greenshielddel()
            player2.purpleshielddel()


    for c in gfw.world.objects_at(gfw.layer.skyozone):#블루충돌
        if collides_distance(player2, c):
            gfw.world.remove((c))
            dead = player2.decrease_life1()
            wav_item.play()


            if dead:  # 게임오버

                end_game()

            player2.redshielddel()#방패제거
            player2.blueshielddel()
            player2.greenshielddel()
            player2.purpleshielddel()


    for d in gfw.world.objects_at(gfw.layer.whiteozone):#그린충돌
        if collides_distance(player2, d):
            gfw.world.remove((d))
            dead = player2.decrease_life2()
            wav_item.play()



            if dead:  # 게임오버

                end_game()

            player2.redshielddel()#방패제거
            player2.blueshielddel()
            player2.greenshielddel()
            player2.purpleshielddel()


    for e in gfw.world.objects_at(gfw.layer.purpleozone):#퍼플충돌
        global CHECK
        if collides_distance(player2, e):
            gfw.world.remove((e))
            dead = player2.decrease_life3()
            wav_item.play()


            if dead:  # 게임오버
                end_game()


            player2.redshielddel()#방패제거
            player2.blueshielddel()
            player2.greenshielddel()
            player2.purpleshielddel()




###############################

# 게임시작,끝########################

def start_game():
    global state,CLEAR,START,CHECK
    if state != STATE_GAME_OVER:
        return
    player2.reset()
    generator2.reset()

    state = STATE_IN_GAME
    global score
    score = 0

    music_bg.repeat_play()

def stageclear():
    global state
    state = STATE_CLEAR
    gfw.push(ending)

def end_game():
    global state,START,CHECK
    state = STATE_GAME_OVER
    CHECK = False
    gfw.push(restart)


    music_bg.stop()

#######################################


# 음악삭제#############
def exit():
    global music_bg, wav_item, explosionsound,getitemsound,clearmusic
    del music_bg
    del explosionsound
    del wav_item
    del getitemsound
    del clearmusic


############################

# 엔터 드로우 업데이트##################### - 이곳에 반드시추가
def enter():
    gfw.world.init(['bg','bg2' ,  'player2', 'ui','redozone','whiteozone','skyozone','purpleozone','arrivepoint'])
    player2.init()
    gfw.world.add(gfw.layer.player2, player2)
    global game_over_image  # 게임오버시
    game_over_image = gfw.image.load('res/game_over.png')

    global font  # 폰트
    font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

    global music_bg, wav_item, explosionsound,getitemsound,clearmusic  # 음악처리
    music_bg = load_music('res/background2.mp3')  # 배경음만mp3
    wav_item = load_wav('res/crush.wav')
    explosionsound = load_wav('res/explosion.wav')
    getitemsound=load_wav('res/item.wav')
    clearmusic = load_wav('res/clearmusic.wav')

    global state
    state = STATE_GAME_OVER  # 드로우에서 처리
    start_game()  # 게임시작상태

    global clear

    clear=gfw.image.load('res/stage2clear.png')


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
        gfw.push(howtostage2)

    if state == STATE_CLEAR:
        clear.draw(get_canvas_width() //2, get_canvas_height()//2)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:#엔터 게임시작
            #music_bg.stop()
            start_game()
        elif e.key == SDLK_SPACE:#스페이스바 다음스테이지
            global CHECK
            CHECK = False




    player2.handle_event(e)

def pause():
    pass

if __name__ == '__main__':
    gfw.run_main()
