from PIL import Image, ImageFont, ImageDraw
import os

def do_ad(string_to_print):
    file_path = 'Path-To-Sample'

    my_img = Image.open(file_path)

    my_img.load()
    draw = ImageDraw.Draw(my_img)
    size = my_img.size
    width = size[0]
    heigth = size[1]
    font = ImageFont.truetype("calibriz.ttf", 36)
    to_show = ' '

    check = True
    for i in range(len(string_to_print)):
        if not check:
            if string_to_print[i] == ' ':
                to_show += '\n'
                check = True
        
        if i%30 == 0 and i>10:
            check = False
        
        to_show += string_to_print[i]

    draw.text((width - (width*0.85), heigth - (heigth*0.95)), to_show,(0,0,0),font=font)
    path_out = 'Path-To-OutImg'
    my_img.save(path_out)
    return path_out