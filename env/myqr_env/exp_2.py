from PIL import Image
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = (265.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open("github.jpg")
    width,hight = im.size
    im = im.resize((width, hight),Image.NEAREST)
    txt = ''
    for i in range(width):
        for j in range(hight):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    with open('output.txt','w') as f:
        f.write(txt)
