import gfw
from pico2d import *
from gobj import *

class HorzScrollBackground:#가로스크롤
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 0

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        left, bottom = 0, 0
        page = self.image.w * self.ch // self.image.h
        curr = int(-self.scroll) % page
        if curr > 0:
            sw = int(1 + self.image.h * curr / self.ch)
            sl = self.image.w - sw
            src = sl, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr - dw, 0, dw, self.ch
            self.image.clip_draw_to_origin(*src, *dst)
        dst_width = round(self.image.w * self.ch / self.image.h)
        while curr + dst_width < self.cw:
            dst = curr, 0, dst_width, self.ch
            self.image.draw_to_origin(*dst)
            curr += dst_width
        if curr < self.cw:
            dw = self.cw - curr
            sw = int(1 + self.image.h * dw / self.ch)
            src = 0, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr, 0, dw, self.ch
            self.image.clip_draw_to_origin(*src, *dst)

    def to_screen(self, point):
        x, y = point
        return x - self.scroll, y

    def translate(self, point):
        x, y = point
        return x + self.scroll, y

    def get_boundary(self):
        return (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)


class VertScrollBackground:#세로스크롤
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 0


    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        left, bottom = 0, 0
        page = self.image.h * self.cw // self.image.w
        curr = int(-self.scroll) % page
        if curr > 0:
            sh = int(1 + self.image.w * curr / self.cw)
            sl = self.image.h - sh
            src = 0, sl, self.image.w , sh
            dh = int(sh * self.cw / self.image.w)
            dst = 0, curr - dh, self.cw, dh
            self.image.clip_draw_to_origin(*src, *dst)
        dst_h = round(self.image.h * self.cw / self.image.w)
        while curr + dst_h < self.ch:
            dst = 0, curr, self.cw, dst_h
            self.image.draw_to_origin(*dst)
            curr += dst_h
        if curr < self.ch:
            dh = self.ch - curr
            sh = int(1 + self.image.w * dh / self.cw)
            src = 0, 0, self.image.w, sh
            dh = int(sh * self.cw / self.image.w)
            dst = 0, curr, self.cw, dh
            self.image.clip_draw_to_origin(*src, *dst)



    #     self.image.clip_draw_to_origin(*self.src_rect_1, *self.dst_rect_1)
    #     self.image.clip_draw_to_origin(*self.src_rect_2, *self.dst_rect_2)

    # private void drawHorizontal(Canvas canvas) {
    #     int left = 0;
    #     int top = 0;
    #     int right = UiBridge.metrics.size.x;
    #     int bottom = UiBridge.metrics.size.y;
    #     int pageSize = sbmp.getWidth() * (bottom - top) / sbmp.getHeight();

    #     canvas.save();
    #     canvas.clipRect(left, top, right, bottom);

    #     float curr = scrollX % pageSize;
    #     if (curr > 0) curr -= pageSize;
    #     curr += left;
    #     while (curr < right) {
    #         dstRect.set(curr, top, curr + pageSize, bottom);
    #         curr += pageSize;
    #         canvas.drawBitmap(sbmp.getBitmap(), srcRect, dstRect, null);
    #     }
    #     canvas.restore();
    # }