#플레이어 무빙효과

import random
from pico2d import *
import gfw
import player

CHECK=True

class Move:

    def __init__(self):
        self.fidx = 1
        if CHECK==True:
            self.image = gfw.image.load('res/player3.png')

    def draw(self):
        px, py = player.pos
        self.image.clip_draw(0, self.fidx,80,70, px , py)
    def update(self):
        self.fidx = (self.fidx-1 ) %8

    def ss(self):
        global CHECK
        CHECK = False

