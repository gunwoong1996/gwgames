##이곳에서 효과처리

from pico2d import *
import gfw
from meteor import Meteor
from rockethead import Rockethead#로켓머리
from rocketbody import Rocketbody#로켓바디
from rocketleft import Rocketleft#로켓바디
from rocketlight import Rocketlight#로켓바디
from shield import Shield#쉴드



import random

METEOR_COUNT = 23

RH=True
RB=True
RL=True
RI=True
RS=True

def RHC():#로켓헤드 사라지게하기
    global RH
    RH=False
def RBC():#로켓바디 사라지게하기
    global RB
    RB=False
def RLC():#로켓왼날 사라지게하기
    global RL
    RL=False
def RRC():#로켓오날 사라지게하기
    global RI
    RI=False
def RSC():#쉴드 사라지게하기
    global RS
    RS=False
def RSM():#쉴드 만들게하기
    global RS
    RS=True
def reset():#재시작시 리셋 시켜주기
    global RH,RB,RL,RI
    RH=True
    RB=True
    RL=True
    RI=True

##운석 속도조절
def update(score):

    max_count = METEOR_COUNT + score / 10

    rockethead_count = 1
    rocketbody_count = 1
    rocketleft_count = 1
    rocketlight_count = 1
    shield_count = 1

    if gfw.world.count_at(gfw.layer.meteor) < max_count:#운석
        generate(score)

    if gfw.world.count_at(gfw.layer.rockethead) <rockethead_count:#로켓머리
        if RH==True:
            generate1(score)

    if gfw.world.count_at(gfw.layer.rocketbody) < rocketbody_count:#로켓바디
        if RB==True:
            generate2(score)

    if gfw.world.count_at(gfw.layer.rocketleft) < rocketleft_count:#로켓왼날
        if RL==True:
            generate3(score)

    if gfw.world.count_at(gfw.layer.rocketlight) < rocketlight_count:#로켓오날
        if RI==True:
            generate4(score)

    if gfw.world.count_at(gfw.layer.shield) < shield_count:#로켓오날
        if RS==True:
            generate5(score)

##운석 등장
def generate(score):
    dx = random.random()
    if dx < 0.9: dx -= 1.0
    dy = random.random()
    if dy < 0.9: dy -= 1.0

    mag = 1 + score / 100 #운석속도조절
    dx *= mag
    dy *= mag

    side = random.randint(1, 4)
    if side == 1: # left
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = -dx
    else: # side == 4: # up
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dy

    m = Meteor((x,y), (dx,dy))
    gfw.world.add(gfw.layer.meteor, m)


#로켓헤드 생성
def generate1(score):
    dx = random.random()
    if dx < 0.9: dx -= 1.0
    dy = random.random()
    if dy < 0.9: dy -= 1.0

    mag = 1 + score / 100
    dx *= mag
    dy *= mag

    side = random.randint(1, 4)
    if side == 1: # left
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = -dx
    else: # side == 4: # up
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dy

    n= Rockethead((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rockethead, n)

#로켓바디 생성
def generate2(score):
    dx = random.random()
    if dx < 0.9: dx -= 1.0
    dy = random.random()
    if dy < 0.9: dy -= 1.0

    mag = 1 + score / 100
    dx *= mag
    dy *= mag

    side = random.randint(1, 4)
    if side == 1: # left
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = -dx
    else: # side == 4: # up
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dy

    c = Rocketbody((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rocketbody, c)

#로켓왼쪽날개 생성
def generate3(score):
    dx = random.random()
    if dx < 0.9: dx -= 1.0
    dy = random.random()
    if dy < 0.9: dy -= 1.0

    mag = 1 + score / 100
    dx *= mag
    dy *= mag

    side = random.randint(1, 4)
    if side == 1: # left
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = -dx
    else: # side == 4: # up
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dy

    d = Rocketleft((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rocketleft, d)


#로켓오른쪽날개 생성
def generate4(score):
    dx = random.random()
    if dx < 0.9: dx -= 1.0
    dy = random.random()
    if dy < 0.9: dy -= 1.0

    mag = 1 + score / 100
    dx *= mag
    dy *= mag

    side = random.randint(1, 4)
    if side == 1: # left
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = -dx
    else: # side == 4: # up
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dy

    c = Rocketlight((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rocketlight, c)


#쉴드아이템생성
def generate5(score):

    dx = random.random()
    if dx < 0.9: dx -= 1.0
    dy = random.random()
    if dy < 0.9: dy -= 1.0

    mag = 1 + score / 100
    dx *= mag
    dy *= mag

    side = random.randint(1, 4)
    if side == 1: # left
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = -dx
    else: # side == 4: # up
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dy

    g =Shield((x,y), (dx,dy))
    gfw.world.add(gfw.layer.shield, g)
