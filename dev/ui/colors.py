import random

# https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python

'''
Method to generate a list of 100k random HEX Colors.
This method was based off a a reply by Eneko Alonso to a stackoverflow question
https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python

Contributors:
Aidan Hayes
'''
def gen_colors():
    colors = []
    for i in range(100000):
        # Generate random hex value
        highlight = "%06x" % random.randint(0, 0xFFFFFF)
        # Add # in front so that it is read as hex value by GUI
        highlight = "#" + highlight
        colors.append(highlight)
    return colors
