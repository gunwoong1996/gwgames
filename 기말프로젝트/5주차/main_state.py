from pico2d import *
import gfw
import player  # 플레이어 및 여러 이미지처리
import generator  # 동작처리
import stage1bg  # 스테이지1배경
from moveplayer import *  # 플레이어움직임

canvas_width = 1000
canvas_height = 800

STATE_IN_GAME, STATE_GAME_OVER = range(2)

##로켓그려주기 체크####
HEAD= False
HEAD1=False
HEAD2=False
HEAD3=False
########################


# 충돌체크########################
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    return distance_sq < radius_sum ** 2


def check_collision():
    global state
    for m in gfw.world.objects_at(gfw.layer.meteor):
        if collides_distance(player, m):
            explosionsound.play()
            gfw.world.remove((m))

            dead = player.decrease_life()
            if dead:
                end_game()

    global HEAD
    for n in gfw.world.objects_at(gfw.layer.rockethead):
        if collides_distance(player, n):
            explosionsound.play()
            gfw.world.remove((n))
            HEAD=True

    global HEAD1
    for c in gfw.world.objects_at(gfw.layer.rocketbody):
        if collides_distance(player, c):
            explosionsound.play()
            gfw.world.remove((c))
            HEAD1 = True

    global HEAD2
    for d in gfw.world.objects_at(gfw.layer.rocketleft):
        if collides_distance(player, d):
            explosionsound.play()
            gfw.world.remove((d))
            HEAD2 = True

    global HEAD3
    for f in gfw.world.objects_at(gfw.layer.rocketlight):
        if collides_distance(player, f):
            explosionsound.play()
            gfw.world.remove((f))
            HEAD3 = True

###############################


# 게임시작,끝########################
def start_game():
    global state
    if state != STATE_GAME_OVER:
        return
    player.reset()
    gfw.world.clear_at(gfw.layer.meteor)

    state = STATE_IN_GAME

    global score
    score = 0

    music_bg.repeat_play()


def end_game():
    global state
    print('Dead')
    state = STATE_GAME_OVER
    music_bg.stop()


#######################################


# 음악삭제#############
def exit():
    global music_bg, wav_item, explosionsound
    del music_bg
    del explosionsound
    del wav_item


############################

# 엔터 드로우 업데이트##################### - 이곳에 반드시추가
def enter():
    gfw.world.init(['stage1bg', 'stage2bg', 'meteor', 'player', 'ui', 'rockethead','rocketbody','rocketleft','rocketlight'])
    player.init()
    gfw.world.add(gfw.layer.player, player)

    ##스테이지
    stage1bg.init()  # 스테이지1삽입
    gfw.world.add(gfw.layer.stage1bg, stage1bg)

    global game_over_image  # 게임오버시
    game_over_image = gfw.image.load('res/game_over.png')

    global font  # 폰트
    font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

    global music_bg, wav_item, explosionsound  # 음악처리
    music_bg = load_music('res/background.mp3')  # 배경음만mp3
    wav_item = load_wav('res/item.wav')
    explosionsound = load_wav('res/explosion.wav')

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


    # 무브

    global move
    move = Move()


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
    # score_pos = 30, get_canvas_height() - 30


    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        game_over_image.draw(*center)

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
    if(HEAD==True and HEAD1 == True and HEAD2 == True and HEAD3 == True):
        end_game()


    # 무브
    move.draw()


#####################################################

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
            start_game()

    player.handle_event(e)


if __name__ == '__main__':
    gfw.run_main()
