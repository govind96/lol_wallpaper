from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
import PIL

font = ImageFont.truetype("/usr/share/fonts/tlwg/Purisa.ttf", 40)
img = Image.new("RGBA", (1920,1080), (200,20,20))
draw = ImageDraw.Draw(img)
width = 1080
height = 1920
x = 0
y = 0
for x in range(0, height, 120):
    for y in range(0, width, 120):
        draw.text((x,y), "LoL", (255,255,0), font=font)

draw = ImageDraw.Draw(img)      
img.save("/home/govind/Pictures/you_can_not_escape.png")

os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/govind/Pictures/you_can_not_escape.png")
