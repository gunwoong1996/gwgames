#로켓바디처리
from pico2d import *
import gfw
import random
MOVE_PPS = 100

class Shield:
    SIZE = 70

    def __init__(self, pos, delta):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load('res/shield.png')
        mag = random.uniform(0.7, 1.0)
        self.radius = mag * self.image.h //2

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        self.pos = x,y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        diameter = 2 * self.radius
        self.image.draw(*self.pos, diameter, diameter)

    #맵상 경계설정
    def in_boundary(self):
        x,y = self.pos
        if x < -Shield.SIZE: return False
        if y < -Shield.SIZE: return False
        if x > get_canvas_width() + Shield.SIZE: return False
        if y > get_canvas_height() + Shield.SIZE: return False
        return True
