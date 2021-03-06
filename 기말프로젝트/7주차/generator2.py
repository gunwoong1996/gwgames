##이곳에서 효과처리

from pico2d import *
import gfw
from redozone import Redozone#쉴드

import random


##운석 속도조절
def update(score):

    max_count = 1

    if gfw.world.count_at(gfw.layer.redozone) < max_count:#운석
            generate(score)


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

    m = Redozone((x,y), (dx,dy))
    gfw.world.add(gfw.layer.redozone, m)






