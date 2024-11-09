from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import Tk
from tkinter.ttk import Frame, Label
import requests
import sys


image = Image.open('jelly.png')
cropped = image.crop((120, 582, 430, 857))
cropped.save('jelly_2.png')
image_2 = Image.open('jelly_2.png')
image_2.show()

import sys

try:
    tatras = Image.open("tatras.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

rotated = tatras.rotate(180)
rotated.save('tatras_rotated.jpg')




class Example(Frame):

    def __init__(self):
        super().__init__()

        self.loadImage()
        self.initUI()

    def loadImage(self):
        try:
            self.img = Image.open("tatras.jpg")

        except IOError:
            print("Unable to load image")
            sys.exit(1)

    def initUI(self):
        self.master.title("Label")

        tatras = ImageTk.PhotoImage(self.img)
        label = Label(self, image=tatras)

        # reference must be stored
        label.image = tatras

        label.pack()
        self.pack()

    def setGeometry(self):
        w, h = self.img.size
        self.master.geometry(("%dx%d+300+300") % (w, h))


def main():
    root = Tk()
    ex = Example()
    ex.setGeometry()
    root.mainloop()


if __name__ == '__main__':
    main()



url = 'https://i.ytimg.com/vi/vEYsdh6uiS4/maxresdefault.jpg'

try:
    resp = requests.get(url, stream=True).raw
except requests.exceptions.RequestException as e:
    sys.exit(1)

try:
    img = Image.open(resp)
except IOError:
    print("Unable to open image")
    sys.exit(1)

img.save('sid.jpg', 'jpeg')




img = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(img)

idraw.rectangle((20, 10, 30, 50), fill='blue')

img.save('rectangle.png')



try:
    tatras = Image.open("tatras.jpg")
except:
    print("Unable to load image")
    sys.exit(1)

idraw = ImageDraw.Draw(tatras)
text = "High Tatras"

font = ImageFont.truetype("arial.ttf", size=18)

idraw.text((10, 10), text, font=font)

tatras.save('tatras_watermarked.png')


try:
    tatras = Image.open("tatras.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

grayscale = tatras.convert('L')
grayscale.show()