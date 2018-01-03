# Add a logo to every image and resize the image to fit 300x300px square

import os
from PIL import Image

os.chdir(r'D:\Python\Programs\Images_lesson')
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo_new.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size


os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if (not (filename.endswith('.png') or filename.endswith('.jpg'))
            or filename == LOGO_FILENAME):
        continue
    im = Image.open(filename)
    width, height = im.size
    if (width > SQUARE_FIT_SIZE) or (height > SQUARE_FIT_SIZE):
        if width > height:
            height = int((SQUARE_FIT_SIZE/width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
    print('Adding a logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('withLogo', filename))

def main():
    pass

if __name__ == '__main__':
    main()
