from pico2d import *
import gfw
import player #플레이어
import generator #동작처리
import stage1bg #스테이지1배경
from moveplayer import * #플레이어움직임

canvas_width=1000
canvas_height=800



STATE_IN_GAME, STATE_GAME_OVER = range(2)



#충돌체크########################
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq =(ax - bx)**2 + (ay - by)**2
    return distance_sq < radius_sum**2

def check_collision():
    global state
    for m in gfw.world.objects_at(gfw.layer.meteor):
        if collides_distance(player , m):
            explosionsound.play()
            gfw.world.remove((m))
            dead = player.decrease_life()
            if dead:
                end_game()
###############################
                
#게임시작,끝########################
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


#음악삭제#############
def exit():
    global music_bg, wav_item, explosionsound
    del music_bg
    del explosionsound
    del wav_item
############################

#엔터 드로우 업데이트#####################
def enter():
    gfw.world.init(['stage1bg', 'meteor', 'player', 'ui'])
    player.init()
    gfw.world.add(gfw.layer.player, player)
    stage1bg.init()#스테이지1삽입
    gfw.world.add(gfw.layer.stage1bg, stage1bg)


    global game_over_image #게임오버시
    game_over_image = gfw.image.load('res/game_over.png')

    global font #폰트
    font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

    global music_bg, wav_item, explosionsound #음악처리
    music_bg = load_music('res/background.mp3')#배경음만mp3
    wav_item = load_wav('res/item.wav')
    explosionsound = load_wav('res/explosion.wav')

    global state
    state = STATE_GAME_OVER #드로우에서 처리
    start_game() #게임시작상태

    #무브

    global move
    move=Move()


def update():
    if state != STATE_IN_GAME:
        return
    global score
    score += gfw.delta_time
    gfw.world.update()
    generator.update(score)
    check_collision()

    #무브

    move.update()

def draw():
    gfw.world.draw()
    #score_pos = 30, get_canvas_height() - 30

    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        game_over_image.draw(*center)

    #무브
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
