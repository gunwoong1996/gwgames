#플레이어 무빙효과

import random
from pico2d import *

import player

RES_DIR ='C:/Users/SeoYM/Desktop/py_03_13_2016180020/res'


class Move:

    def __init__(self):
        self.fidx = 1
        self.image = load_image(RES_DIR + '/player3.png')
    def draw(self):
        px, py = player.pos
        self.image.clip_draw(0, self.fidx,80,70, px , py)
    def update(self):
        self.fidx = (self.fidx-1 ) %8

