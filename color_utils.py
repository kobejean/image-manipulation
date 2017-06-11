# code from: https://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa

import tensorflow as tf

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(r, g, b):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (r, g, b)

def rgb_to_hsv(r,g,b):
    return colorsys.rgb_to_hsv(r/255,g/255,b/255)

def hsv_to_rgb(h,s,v):
    (r,g,b) = colorsys.hsv_to_rgb(h,s,v)
    return (int(r*255), int(g*255), int(b*255))
