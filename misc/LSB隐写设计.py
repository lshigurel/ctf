'''
实现LSB数据隐藏算法,对图片base.png添加字符串数据'hello world'
'''

from PIL import Image

img = Image.open('base.png')

def get_pixel(x, y):
    return img.getpixel((x, y))

def set_pixel(x, y, color):
    img.putpixel((x, y), color)

def main():
    water_str = b'hello world'
    water_bin_str = ''.join([bin(i)[2:].zfill(8) for i in water_str])
    print(water_bin_str)

    height, width = img.height, img.width
    x = 0

    for j in range(height):
        for i in range(width):
            color = get_pixel(i, j)
            
            if x >= len(water_bin_str):
                continue

            if x + 3 < len(water_bin_str):
                _str = water_bin_str[x:x+3]
            else:
                _str = water_bin_str[x:] + '000'
                
            x += 3
            new_color = (
                color[0] & 0xFE | int(_str[0]), 
                color[1] & 0xFE | int(_str[1]), 
                color[2] & 0xFE | int(_str[2])
            )

            print('write {} to ({}, {})'.format(_str, i, j))
            set_pixel(i, j, new_color)

    img.save('watermark.png')
    img.show()

if __name__ == '__main__':
    main()
