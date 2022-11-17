import random

# https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python

def gen_colors():
    colors = []
    for i in range(100000):
        highlight = "%06x" % random.randint(0, 0xFFFFFF)
        highlight = "#" + highlight
        colors.append(highlight)
        # print(highlight)
    return colors
