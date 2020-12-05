#플레이어처리

from pico2d import *
import gfw
import generator2


MOVE_PPS = 200
MOVE_PPS1 = 0
MAX_LIFE = 5


RED=False
BLUE=False
GREEN=False
PURPLE=False
ALL=False

CHECK1=True
CHECK2=True
CHECK3=True
CHECK4=True
############쉴드효과####################
def redshieldora():
    global CHECK1
    CHECK1=False

def blueshieldora():
    global CHECK2

    CHECK2 = False

def greenshieldora():
    global CHECK3
    CHECK3 = False

def purpleshieldora():
    global CHECK4
    CHECK4 = False
#########################

############쉴드제거###################
def redshielddel():
    global RED,CHECK1
    RED=False
    CHECK1=True
def blueshielddel():
    global BLUE,CHECK2
    BLUE=False
    CHECK2 = True

def greenshielddel():
    global GREEN,CHECK3
    GREEN=False
    CHECK3 = True

def purpleshielddel():
    global PURPLE,CHECK4
    PURPLE=False
    CHECK4 = True
#########################

############쉴드생성####################
def redshield():
    global RED
    RED=True


def blueshield():
    global BLUE
    BLUE=True


def greenshield():
    global GREEN
    GREEN=True

def purpleshield():
    global PURPLE
    PURPLE=True


#########################
def init():
    global image,image1, pos, radius,radius1,location,red,blue,green,purple

    image = gfw.image.load('res/rocket2.png')#플레이어
    image1 = gfw.image.load('res/player.png') # 플레이어
    location=gfw.image.load('res/location.png')#위치

    red=gfw.image.load('res/redshield.png')#레드쉴드
    blue= gfw.image.load('res/blueshield.png')#블루쉴드
    green = gfw.image.load('res/greenshield.png')  # 블루쉴드
    purple = gfw.image.load('res/purpleshield.png')  # 블루쉴드

    global oilgauge, oilgaugedel
    oilgauge = gfw.image.load('res/oilgauge.png')

    oilgaugedel = gfw.image.load('res/oilgaugedel.png')

    radius = image.h // 2
    radius1 = image1.h // 2


    reset()

def reset():
    global image, pos, radius,pos1,radius1
    pos = get_canvas_width()-1000 , get_canvas_height() //2
    pos1 = get_canvas_width() , get_canvas_height()

    global delta_x, delta_y,delta_x1, delta_y1
    delta_x, delta_y = 0, 0
    delta_x1, delta_y1=0,0

    global life
    life = MAX_LIFE

def decrease_life():
    global life

    if CHECK1==True:
        life -= 1
        return life <= 0

def decrease_life1():
    global life

    if CHECK2==True:
        life -= 1
        return life <= 0

def decrease_life2():
    global life

    if CHECK3==True:
        life -= 1
        return life <= 0

def decrease_life3():
    global life

    if CHECK4==True:
        life -= 1
        return life <= 0


def update():
    global pos, delta_x, delta_y,pos1, delta_x1, delta_y1
    x, y = pos
    x += delta_x * MOVE_PPS * gfw.delta_time
    y += delta_y * MOVE_PPS * gfw.delta_time

    hw, hh = image.w // 2, image.h // 2
    x = clamp(hw, x, get_canvas_width() - hw)
    y = clamp(hh, y, get_canvas_height() - hh)
    pos = x, y

    #################

    x1, y1 = pos1
    x1 += delta_x1 * MOVE_PPS1 * gfw.delta_time
    y1 += delta_y1 * MOVE_PPS1 * gfw.delta_time

    hw1, hh1 = image1.w // 2, image1.h // 2
    x1 = clamp(hw, x1, get_canvas_width() - hw1)
    y1 = clamp(hh, y1, get_canvas_height() - hh1)
    pos1 = x1, y1



def draw():
    global image, pos,pos1,RED,BLUE,GREEN,PURPLE
    image.draw(*pos)#플레이어
    image1.draw(*pos1)  # 플레이어
    location.draw(get_canvas_width()-130 ,get_canvas_height()-20)  # 플레이어



    ##연료게이지##
    x, y = get_canvas_width()-965, get_canvas_height()-30

    for i in range(MAX_LIFE):
        oil = oilgauge if i < life else oilgaugedel
        oil.draw(x, y)
        x+=50




    if(RED==True):
        red.draw(*pos)  #레드쉴드

    if(BLUE == True):
        blue.draw(*pos)  #블루쉴드

    if (GREEN == True):
        green.draw(*pos)  # 그린쉴드

    if (PURPLE == True):
        purple.draw(*pos)  # 보라쉴드


def handle_event(e):
    global delta_x, delta_y,RED,BLUE,GREEN,PURPLE

    if e.type == SDL_KEYDOWN:
        if e.key ==  SDLK_q:#레드쉴드
            redshield()
            redshieldora()

            BLUE=False
            GREEN=False
            PURPLE=False
        elif e.key == SDLK_w:#블루쉴드
            blueshield()
            blueshieldora()

            RED = False
            GREEN = False
            PURPLE = False
        elif e.key == SDLK_e:#그린쉴드
            greenshield()
            greenshieldora()

            RED = False
            BLUE = False
            PURPLE = False
        elif e.key == SDLK_r:#보라쉴드
            purpleshield()
            purpleshieldora()

            RED = False
            BLUE = False
            GREEN = False
    elif e.type == SDL_KEYUP:
        if e.key ==  SDLK_q:
            redshield()
            redshieldora()

            BLUE = False
            GREEN = False
            PURPLE = False
        elif e.key == SDLK_w:
            blueshield()
            blueshieldora()

            RED = False
            GREEN = False
            PURPLE = False
        elif e.key == SDLK_e:
            greenshield()
            greenshieldora()

            RED = False
            BLUE = False
            PURPLE = False
        elif e.key == SDLK_r:
            purpleshield()
            purpleshieldora()

            RED = False
            BLUE = False
            GREEN = False
