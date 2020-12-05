
from pico2d import *
import gfw
import random
MOVE_PPS =80
MOVE_PPS1 =0
class Redozone:
    SIZE = 300

    def __init__(self, pos, delta):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load('res/redozone.png')
        self.radius =self.image.w-110+ self.image.h//2

    def update(self):
        x, y = self.pos
        dx = self.delta
        dy = self.delta
        x -= dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS1 * gfw.delta_time
        self.pos = x, y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        self.image.draw(*self.pos, 10, 700)

    #맵상 경계설정
    def in_boundary(self):
        x,y = self.pos
        if x < -Redozone.SIZE: return False
        if y < -Redozone.SIZE: return False
        if x > get_canvas_width() + Redozone.SIZE: return False
        if y > get_canvas_height() + Redozone.SIZE: return False
        return True
