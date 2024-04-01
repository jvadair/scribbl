from machine import Pin, SPI
import gc9a01  # Display driver
from lib.i2cdrivers import CST816, QMI8658C  # Touch and 6-axis sensor drivers
import gc
from time import sleep

from apps import clock as _default  # You can change 'clock' to whatever app you want!

display = gc9a01.GC9A01(
            SPI(2, baudrate=80000000, polarity=0, sck=Pin(10), mosi=Pin(11)),
            240,
            240,
            reset=Pin(14, Pin.OUT),
            cs=Pin(9, Pin.OUT),
            dc=Pin(8, Pin.OUT),
            backlight=Pin(2, Pin.OUT),
            rotation=3,
            buffer_size=16*32*2
        )

display.init()
touch = CST816()
q = QMI8658C()


# Boot
display.jpg('scribblOS.jpg', 0, 0, gc9a01.SLOW)
sleep(1)
display.fill(gc9a01.BLACK)
display.off()


while True:
    sleep(0.05)
    if touch.get_touch() or q.Read_XYZ()[1] > .9:  # Activate on touch or wrist-rotate
        display.on()
        _default.run(display, touch, q)
        display.off()
        sleep(.3)
        
