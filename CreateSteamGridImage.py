from PIL import Image, ImageDraw, ImageFont
import os

root_dir = 'C:/Users/ZLHys/ROMs/GB/roms'
output_dir = 'C:/Users/ZLHys/PycharmProjects/MakeBats/dist/GB/Images/'
for filename in os.listdir(root_dir):
    print("Creating Steam Grid Image for: " + os.path.splitext(filename)[0])

    W, H = (920, 430)

    msg = os.path.splitext(filename)[0]

    img = Image.new('RGB', (W, H), 'black')

    bg = Image.open('snes.jpg', 'r')
    img_w, img_h = img.size
    bg_w, bg_h = bg.size
    offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)

    img.paste(bg)

    text = ImageDraw.Draw(img)

    name_font = ImageFont.truetype('VINERITC.TTF', 55)
    w, h = name_font.getsize(msg)
    text.text(((W-w)/2, (H-h)/2), msg, font=name_font, fill=(0, 0, 0))

    img.save(output_dir + os.path.splitext(filename)[0] + '.png')
