import os
from PIL import Image, ImageChops
import time


if os.path.exists("Background") and os.path.exists("Body"):
    if(os.path.exists("Train")==False):
        os.mkdir("Train")
        os.mkdir("Train/Body")
        os.mkdir("Train/Background")
    for name in os.listdir("Body/"):
        image = Image.open("Body/"+name)
        ancho,largo= image.size
        ret = True
        left=0
        top=0
        while largo-top>=3:
            while ancho-left>=3:
                im = image.crop((left,top,left+3,top+3)
                im.save("Train/Body/"+str(time.time())+".jpg")
                left = left + 3
            top = top + 3
            left=0
    for name in os.listdir("Background/"):
        image = Image.open("Background/"+name)
        ancho,largo= image.size
        ret = True
        left=0
        top=0
        while largo-top>=3:
            while ancho-left>=3:
                im = image.crop((left,top,left+3,top+3)
                im.save("Train/Background/"+str(time.time())+".jpg")
                left = left + 3
            top = top + 3
            left=0
        
            
        
        