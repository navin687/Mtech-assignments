# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:16:44 2021

@author: nkd
"""

from PIL import Image
import numpy as np

img = Image.open("third.jpg").convert('L')
#img.show()

biggest = np.amax(img)
#print(biggest)
width, height = img.size
a=int(biggest/4)

for i in range(width):
    for j in range(height):
       value=img.getpixel((i,j))
       #print(val)
       if value>=0 and value<a:
           img.putpixel((i,j),0)
       elif value>=a and value<(2*a):
           img.putpixel((i,j),a)
       elif value>=2*a and value<3*a:
           img.putpixel((i,j),2*a)
       elif value>=3*a and value<(4*a-1):
           img.putpixel((i,j),3*a)
       else:
           img.putpixel((i,j),255)
img.save("third_new.jpg")           
img.show()