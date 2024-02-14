from machine import Pin, SPI
import gc9a01  # Display driver
import time
from i2cdrivers import CST816, QMI8658C  # Touch and 6-axis sensor drivers
from truetype import NotoSans_32 as noto_sans
import network
import requests
import ntptime
import gc

UTC_OFFSET = -5 * 60 * 60  # EST
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Dec')
WEEK = ('Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat')


tft = gc9a01.GC9A01(
        SPI(2, baudrate=80000000, polarity=0, sck=Pin(10), mosi=Pin(11)),
        240,
        240,
        reset=Pin(14, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(2, Pin.OUT),
        rotation=3,
        buffer_size=16*32*2)


tft.init()
touch = CST816()
q = QMI8658C()
touch_released = True
tft.fill(gc9a01.BLACK)
tft.off()
touch_released = True



def real_time():
    return time.localtime(time.time() + UTC_OFFSET)


def center(font, s, color=gc9a01.WHITE, x=None, y=None):
        if x is None:
            screen_width = tft.width()               # get screen width
            width = tft.write_len(font, s)           # get the width of the string
            if width and width < screen_width:       # if the string < display
                x = screen_width // 2 - width // 2    # find the column to center
            else:                                    # otherwise
                x = 0                                # left justify
        if y is None:
            screen_height = tft.height()
            y = screen_height // 2 - 16  # - half the size of the font

        tft.write(font, s, x, y, color)      # and write the string
        
def zfill(s):
    if type(s) is int:
        s = str(s)
    return s if len(s) > 1 else '0' + s


def wait_for_touch(func, s=0, frequency=50, function_controlled=False, initial_parameter=None):  # Run function until press or <s> seconds
    global touch_released
    touch_released=False
    sleep_time = 0
    while sleep_time < s or not s:
        if sleep_time == 0 and initial_parameter is not None:
            function_result = func(initial_parameter)
        else:
            function_result = func()
        sleep_time += 1
        for i in range(0,frequency):
            time.sleep(1/frequency)
            if touch.get_touch():
                if touch_released:
                    touch_released = False
                    if function_controlled and function_result is not True:
                        pass
                    else:
                        point = touch.get_point()
                        point = (240-point.y_point, point.x_point)  # Convert because of flipped display
                        return point
            else:
                touch_released = True


def render_clock():
    global MONTHS
    t = real_time()
    text = "{h}:{m}:{s}".format(h=zfill(t[3]), m=zfill(t[4]), s=zfill(t[5]))
    center(noto_sans, text, y=tft.height() // 2 - 32, color=gc9a01.WHITE)
    month = MONTHS[t[1]-1]
    text = "{month} {date}".format(month=month, date=t[2])
    center(noto_sans, text, y=tft.height() // 2 + 32, color=gc9a01.WHITE)
    


# def show_clock():
#     global touch_released
#     touch_released = False
#     sleep_time = 0
#     while sleep_time < 15:
#         render_clock()
#         sleep_time += 1
#         n = 10  # Defines frequency of press check
#         for i in range(0,n):
#             time.sleep(1/n)
#             if touch.get_touch():
#                 if touch_released:
#                     touch_released = False
#                     return
#             else:
#                 touch_released = True


def show_clock():
    point = wait_for_touch(render_clock, s=15)
    if point:
        show_paper_control()


def handle_epaper_touch(point):
    try:
        if point[1] > 170:
            if point[0] < tft.width() // 2:
                pass
            else:
                return True
        elif point[0] < tft.width() // 2:
            requests.post("http://zeropaper.local:8888", data="previous", timeout=1.5)
        else:
            requests.post("http://zeropaper.local:8888", data="next", timeout=1.5)
    except:
        pass
    return False


def show_paper_control():
    global touch_released
    tft.jpg('control_epaper.jpg', 0, 0, gc9a01.SLOW)
    touch_released = False
#     point = wait_for_touch(handle_epaper_touch, s=15, function_controlled=True, initial_parameter=True)
    while True:
        time.sleep(0.05)
        touched = touch.get_touch()
        if touched and touch_released:
            point = touch.get_point()
            point = (240-point.y_point, point.x_point)  # Convert because of flipped display
            gohome = handle_epaper_touch(point)
            if gohome:
                return
        elif not touched:
            touch_released = True
                


tft.on()
tft.jpg('scribblOS.jpg', 0, 0, gc9a01.SLOW)
wlan = network.WLAN(network.STA_IF) # create station interface
if not wlan.active():
    print('Activating WLAN interface')
    wlan.active(True)
if wlan.isconnected():
    print('Connected to ' + wlan.config('ssid'))
    ntptime.settime()
else:
    network_file = open('wifi.txt', 'r').readlines()
    saved_networks = []
    for line in network_file:
        line = line.split(':::')
        saved_networks.append((line[0], line[1]))
    for SSID, password in saved_networks:
        for i in range(0,3):  # Wait for network
            try:
                wlan = network.WLAN(network.STA_IF)
                wlan.connect(SSID, password) # connect to an AP
            except OSError:
                time.sleep(1)
            if wlan.isconnected():
                break
        if wlan.isconnected():
            ntptime.settime()
            print('Connected to: ' + SSID)
            break
        else:
            print('Failed to connect to ' + SSID)
last_timesync = time.time()
time.sleep(1)  # Give the board a second to load everything into memory and get settled
tft.fill(gc9a01.BLACK)
tft.off()
gc.collect()
while True:
    time.sleep(0.1)
    
    if time.time() - last_timesync > 3600:  # 1 hour
        if wlan.isconnected():
            print('Syncing time')
            ntptime.settime()
        last_timesync = time.time()
    
    if q.Read_XYZ()[1] > .9 or touch.get_touch():
        tft.on()
        show_clock()
        tft.fill(gc9a01.BLACK)
        tft.off()
        while touch.get_touch():
            time.sleep(.1)

# tft.on()
# point = None
# tft.jpg('scribblOS.jpg', 0, 0, gc9a01.SLOW)
# time.sleep(2)
# tft.fill(gc9a01.BLACK)
# while True:
#     if type(point) is tuple:  # If point was just processed
#         prev_point = point
#     else:
#         prev_point = None
#     t = touch.get_touch()
#     point = touch.get_point()
#     gesture = touch.get_gesture()
#     distance = touch.get_distance()
#     
#     
#     if t:
#         point = (240-point.y_point, point.x_point)  # Convert because of flipped display
#         if not prev_point:
#             prev_point = point
#         tft.line(prev_point[0], prev_point[1], point[0], point[1], gc9a01.GREEN)
