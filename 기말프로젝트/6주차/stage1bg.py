#스테이지1배경효과

from pico2d import *
import gfw
import player



def init():
    global space, man
    space = gfw.image.load('res/space.png')

    
def draw():
    
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    
    px, py = player.pos
    dx, dy = x - px, y - py
    space.draw(x + dx * 0.05, y + dy * 0.05)
  
 

def update():
    pass


