##이곳에서 효과처리

from pico2d import *
import gfw
from meteor import Meteor
from rockethead import Rockethead#로켓머리
from rocketbody import Rocketbody#로켓바디
from rocketleft import Rocketleft#로켓바디
from rocketlight import Rocketlight#로켓바디

import random

METEOR_COUNT = 20


##운석 속도조절
def update(score):

    max_count = METEOR_COUNT + score / 10

    rockethead_count = 1
    rocketbody_count = 1
    rocketleft_count = 1
    rocketlight_count = 1

    if gfw.world.count_at(gfw.layer.meteor) < max_count:#운석
        generate(score)

    if gfw.world.count_at(gfw.layer.rockethead) <rockethead_count:#운석
        generate1(score)

    if gfw.world.count_at(gfw.layer.rocketbody) < rocketbody_count:#운석
        generate2(score)

    if gfw.world.count_at(gfw.layer.rocketleft) < rocketleft_count:#운석
        generate3(score)

    if gfw.world.count_at(gfw.layer.rocketlight) < rocketlight_count:#운석
        generate4(score)

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

    n= Rockethead((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rockethead, n)

#로켓바디 생성
def generate2(score):
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

    c = Rocketbody((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rocketbody, c)

#로켓왼쪽날개 생성
def generate3(score):
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

    d = Rocketleft((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rocketleft, d)

#로켓오른쪽날개 생성
def generate4(score):
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

    c = Rocketlight((x,y), (dx,dy))
    gfw.world.add(gfw.layer.rocketlight, c)