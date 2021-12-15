import sys
from PIL import Image
from textwrap import wrap

input_image = sys.argv[1]
output_txt = sys.argv[2]
new_width = int(sys.argv[3])


def get_char(pixel):
    if pixel >= 0 and pixel < 51:
        return 0
    elif pixel >= 51 and pixel < 102:
        return 1
    elif pixel >= 102 and pixel < 153:
        return 2
    elif pixel >= 153 and pixel < 204:
        return 3
    else:
        return 4



def get_image():
    
    img = Image.open(input_image)
    img = img.convert('L')


    width, height = img.size
    aspect_ratio = height/width
    
    new_height = aspect_ratio * new_width * 0.60
    img = img.resize((new_width, int(new_height)))
    
    return img


def main():
    img = get_image()
    pixels = img.getdata()
    chars = ['.',':','+', '*', '#']
    pixels_in_ascii = ''.join([chars[get_char(pixel)] for pixel in pixels])


    ascii_image = wrap(pixels_in_ascii, new_width)

    with open(output_txt, 'w') as file:
        file.write('\n'.join(ascii_image))



if __name__ == "__main__":
    main()