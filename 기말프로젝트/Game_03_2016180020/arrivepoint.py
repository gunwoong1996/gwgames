
from pico2d import *
import gfw
import random
MOVE_PPS =2.0
MOVE_PPS1 =0

class Arrivepoint:
    SIZE = 100

    def __init__(self, pos1, delta):
        self.pos1 = pos1
        self.delta = delta
        self.image = gfw.image.load('res/arrive.png')
        self.radius =self.image.w-120+ self.image.h//2

    def update(self):
        x, y = self.pos1
        dx = self.delta
        dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS1 * gfw.delta_time
        self.pos1 = x, y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        self.image.draw(*self.pos1,30,30)


    #맵상 경계설정
    def in_boundary(self):
        x,y = self.pos1
        if x < -Arrivepoint.SIZE: return False
        if y < -Arrivepoint.SIZE: return False
        if x > get_canvas_width() + Arrivepoint.SIZE: return False
        if y > get_canvas_height() + Arrivepoint.SIZE: return False
        return True

class Arrivepoint1:
    SIZE = 100

    def __init__(self, pos1, delta):
        self.pos1 = pos1
        self.delta = delta
        self.image = gfw.image.load('res/arrive.png')
        self.radius =self.image.w-120+ self.image.h//2

    def update(self):
        x, y = self.pos1
        dx = self.delta
        dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS1 * gfw.delta_time
        self.pos1 = x, y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        self.image.draw(*self.pos1,30,30)


    #맵상 경계설정
    def in_boundary(self):
        x,y = self.pos1
        if x < -Arrivepoint1.SIZE: return False
        if y < -Arrivepoint1.SIZE: return False
        if x > get_canvas_width() + Arrivepoint1.SIZE: return False
        if y > get_canvas_height() + Arrivepoint1.SIZE: return False
        return True
