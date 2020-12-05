##이곳에서 효과처리

from pico2d import *
import gfw
from redozone import Redozone#레드오존
from skyozone import Skyozone#파란오존
from whiteozone import Whiteozone#그린오존
from purpleozone import Purpleozone#보라오존
from arrivepoint import Arrivepoint#위치객체


# import random

CHECK=True


def reset():
    global CHECK
    CHECK=True

def out():
    global CHECK
    CHECK=False

##운석 속도조절
def update(score):

    red_count = 1#레드
    white_count = 1#화이트
    sky_count = 1#스카이
    purple_count = 1  # 스카이
    if CHECK==True:
        arrive_count=1#현재위치
    if CHECK==False:
        arrive_count =0 #현재위치


    if gfw.world.count_at(gfw.layer.redozone) < red_count:#레드

        generatered(score)
    if gfw.world.count_at(gfw.layer.whiteozone) < white_count:#화이트

        generatewhite(score)
    if gfw.world.count_at(gfw.layer.skyozone) < sky_count:#하늘

        generatesky(score)
    if gfw.world.count_at(gfw.layer.purpleozone) < purple_count:  # 보라

        generatepurple(score)

    if gfw.world.count_at(gfw.layer.arrivepoint) < arrive_count: #위치
        if CHECK==True:
            generatearrive(score)


def generatered(score):#레드오존
    dx =1
    mag =1
    dx += mag

    side = 1
    if side == 1:  # left
        x = get_canvas_width()
        y = get_canvas_height() // 2
        if dx < 0: -dx

    m = Redozone((x, y),(dx))
    gfw.world.add(gfw.layer.redozone, m)



def generatewhite(score):#하얀오존
    dx1 = 1
    mag1 = 1  #운석속도조절
    dx1 += mag1

    side = 1
    if side == 1:  # left
        x = get_canvas_width() - 110
        y = get_canvas_height() // 2
        if dx1 < 0: -dx1

    n =Whiteozone((x, y),(dx1))
    gfw.world.add(gfw.layer.whiteozone, n)



def generatesky(score):#하늘오존
    dx2 =1
    mag2 = 1
    dx2 += mag2

    side =1
    if side == 1: # left
        x = get_canvas_width() - 250
        y = get_canvas_height() // 2
        if dx2 < 0: -dx2

    c = Skyozone((x, y),(dx2))
    gfw.world.add(gfw.layer.skyozone, c)


def generatepurple(score):#보라오존
    dx2 =1
    mag2 = 1
    dx2 += mag2

    side =1
    if side == 1: # left
        x = get_canvas_width() - 350
        y = get_canvas_height() // 2
        if dx2 < 0: -dx2

    c = Purpleozone((x, y),(dx2))
    gfw.world.add(gfw.layer.purpleozone, c)


def generatearrive(score):#위치이동

    dx3 =1
    mag3 = 1
    dx3 += mag3


    side = 1
    if side == 1: # left
        x = get_canvas_width() - 220
        y = get_canvas_height()-21
        if dx3 > 0:
            dx3

    if CHECK == True:
        d = Arrivepoint((x, y),(dx3))
        gfw.world.add(gfw.layer.arrivepoint, d)




