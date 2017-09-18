from os import system
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from random import randint


font = ImageFont.truetype("/usr/share/fonts/tlwg/Purisa.ttf", 40)
r = randint(0, 256)
g = randint(0, 256)
b = randint(0, 256)
img = Image.new("RGBA", (1920, 1080), (r, g, b))
draw = ImageDraw.Draw(img)
width = 1080
height = 1920
x = 0
y = 0
r = randint(0, 256)
g = randint(0, 256)
b = randint(0, 256)
for x in range(0, height, 120):
    for y in range(0, width, 120):
        draw.text((x,y), "LoL", (r, g, b), font = font)

draw = ImageDraw.Draw(img)      
img.save("/home/user/.config/you_can_not_escape.png")
