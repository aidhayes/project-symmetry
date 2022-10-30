import random

# https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python
def gen_color():
    highlight = "%06x" % random.randint(0, 0xFFFFFF)
    highlight = "#" + highlight
    print(highlight)
    return highlight