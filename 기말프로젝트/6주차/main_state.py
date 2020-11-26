from pico2d import *
import gfw
import player  # 플레이어 및 여러 이미지처리
import generator  # 동작처리
import howtostage2  # 스테이지2설명

from stage1bg import VertScrollBackground

import gobj
from moveplayer import*
canvas_width = 1000
canvas_height = 700


STATE_IN_GAME, STATE_GAME_OVER = range(2)

CHECK=True#게임오버시 플레이어삭제
CRUSHOFF=True#스테이지클리어시 충돌x


##로켓및 아이템그려주기 체크####
HEAD= False
HEAD1=False
HEAD2=False
HEAD3=False
SHIELD=False
########################

# 충돌체크########################
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    return distance_sq < radius_sum ** 2


def check_collision():
    global state,CRUSHOFF

    if CRUSHOFF==True:
        global SHIELD  # 쉴드충돌
        for g in gfw.world.objects_at(gfw.layer.shield):
            if collides_distance(player, g):
                getitemsound.play()
                gfw.world.remove((g))
                SHIELD = True
                if SHIELD == True:#쉴드생성
                    generator.RSC()
                    player.shieldora()

    if CRUSHOFF == True:
        for m in gfw.world.objects_at(gfw.layer.meteor):#운석충돌
            if collides_distance(player, m):
                explosionsound.play()
                gfw.world.remove((m))

                dead = player.decrease_life()
                if dead:#게임오버
                    end_game()
                if SHIELD == True:#쉴드부딪히면파괴
                    player.crushshield()
                    generator.RSM()


    global HEAD #로켓헤드충돌
    for n in gfw.world.objects_at(gfw.layer.rockethead):
        if collides_distance(player, n):
            wav_item.play()
            gfw.world.remove((n))
            HEAD=True
            if HEAD ==True:
                generator.RHC()

    global HEAD1 #로켓바디 충돌
    for c in gfw.world.objects_at(gfw.layer.rocketbody):
        if collides_distance(player, c):
            wav_item.play()
            gfw.world.remove((c))
            HEAD1 = True
            if HEAD1 ==True:
                generator.RBC()

    global HEAD2 #로켓 왼쪽날개 충돌
    for d in gfw.world.objects_at(gfw.layer.rocketleft):
        if collides_distance(player, d):
            wav_item.play()
            gfw.world.remove((d))
            HEAD2 = True
            if HEAD2 ==True:
                generator.RLC()

    global HEAD3 #로켓 오른쪽날개 충돌
    for f in gfw.world.objects_at(gfw.layer.rocketlight):
        if collides_distance(player, f):
            wav_item.play()
            gfw.world.remove((f))
            HEAD3 = True
            if HEAD3 ==True:
                generator.RRC()


###############################


# 게임시작,끝########################
def start_game():
    global state,CLEAR,HEAD,HEAD1,HEAD2,HEAD3,CHECK
    if state != STATE_GAME_OVER:
        return
    CHECK=True
    player.reset()
    generator.reset()
    HEAD = False
    HEAD1 = False
    HEAD2 = False
    HEAD3 = False

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
    global state1,CHECK,CRUSHOFF
    generator.MED()
    generator.RSC()
    CHECK = False#플레이어제거
    CRUSHOFF=False#충돌제거
    player.crushshield()#방패깨기
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
    gfw.world.init(['bg','bg2' , 'meteor', 'player', 'ui', 'rockethead','rocketbody','rocketleft','rocketlight',
                    'shield'])
    player.init()
    gfw.world.add(gfw.layer.player, player)
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


    #로켓그려주기
    global rockethead
    rockethead = gfw.image.load('res/rockethead.png')

    global rocketbody
    rocketbody = gfw.image.load('res/rocketbody.png')

    global rocketleft
    rocketleft = gfw.image.load('res/rocketleft.png')

    global rocketlight
    rocketlight = gfw.image.load('res/rocketlight.png')

    global shield
    shield = gfw.image.load('res/shieldora.png')


    # 무브

    global move
    move = Move()

    bg =VertScrollBackground('space.png')
    bg.speed = 100
    gfw.world.add(gfw.layer.bg, bg)

    bg = VertScrollBackground('spacedust.png')
    bg.speed = 150
    gfw.world.add(gfw.layer.bg2, bg)


def update():
    if state != STATE_IN_GAME:
        return
    global score
    score += gfw.delta_time
    gfw.world.update()
    generator.update(score)
    check_collision()


    # 무브

    move.update()

def draw():
    gfw.world.draw()

    if state == STATE_GAME_OVER:
        game_over_image.draw(get_canvas_width() //2, get_canvas_height()//2)

#######로켓그려주기################################################################
    if HEAD == True:
        rockethead.draw(get_canvas_width() -930, get_canvas_height()-50)
    if HEAD1 == True:
        rocketbody.draw(get_canvas_width() -930, get_canvas_height()-97)
    if HEAD2 == True:
        rocketleft.draw(get_canvas_width() -958, get_canvas_height()-165)
    if HEAD3 == True:
        rocketlight.draw(get_canvas_width() -900, get_canvas_height()-165)

#####모두 모았을시 다음스테이지#########################
    if (HEAD == True and HEAD1 == True and HEAD2 == True and HEAD3 == True):
        clearstage()
        music_bg.stop()
        stage1clear.draw(get_canvas_width() //2, get_canvas_height()//2)

    # 무브
    if CHECK==True:
        move.draw()


#####################################################

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




    player.handle_event(e)

def pause():
    pass

if __name__ == '__main__':
    gfw.run_main()
