from time import sleep
from lib.realtime import realtime
from lib.zfill import zfill
from lib.graphics import center, noto_sans
import gc9a01


NAME = "Clock"
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Dec')
WEEK = ('Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat')



def run(display, touch, q):
    sleep_time = 0
    touch_released = False
    while sleep_time < 15:
        render_clock(display)
        sleep_time += .1
        sleep(.1)
        if touch.get_touch():
            if touch_released:
                touch_released = False
                return
        else:
            touch_released = True
            
def render_clock(display):
    global MONTHS
    t = realtime()
    text = "{h}:{m}:{s}".format(h=zfill(t[3]), m=zfill(t[4]), s=zfill(t[5]))
    center(display, noto_sans, text, y=display.height() // 2 - 32, color=gc9a01.WHITE)
    month = MONTHS[t[1]-1]
    text = "{month} {date}".format(month=month, date=t[2])
    center(display, noto_sans, text, y=display.height() // 2 + 32, color=gc9a01.WHITE)
    
