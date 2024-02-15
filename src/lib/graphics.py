import gc9a01
from truetype import NotoSans_32 as noto_sans

def center(display, font, s, color=gc9a01.WHITE, x=None, y=None):
        if x is None:
            screen_width = display.width()               # get screen width
            width = display.write_len(font, s)           # get the width of the string
            if width and width < screen_width:       # if the string < display
                x = screen_width // 2 - width // 2    # find the column to center
            else:                                    # otherwise
                x = 0                                # left justify
        if y is None:
            screen_height = display.height()
            y = screen_height // 2 - 16  # - half the size of the font

        display.write(font, s, x, y, color)      # and write the string
        
