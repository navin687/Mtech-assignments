# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:23:56 2021

@author: nkd
"""

from PIL import Image
import numpy as np

img=Image.open("third.jpg").convert('L')
#img.show()

biggest = np.amax(img)
#print(biggest)
width, height = img.size
new=int(biggest/8)
for i in range(width):
    for j in range(height):
       value = img.getpixel((i,j))
       #print(val)
       if value>=0 and value<new:
           img.putpixel((i,j),0)
       elif value>=new and value<(2*new):
           img.putpixel((i,j),new)
       elif value>=2*new and value<(3*new):
           img.putpixel((i,j),2*new)
       elif value>=3*new and value<(4*new):
           img.putpixel((i,j),3*new)
       elif value>=4*new and value<(5*new):
           img.putpixel((i,j),4*new)
       elif value>=5*new and value<(6*new):
           img.putpixel((i,j),5*new)
       elif value>=6*new and value<(7*new):
           img.putpixel((i,j),6*new)
       elif value>=7*new and value<(8*new-1):
           img.putpixel((i,j),7*new)
       else:
           img.putpixel((i,j),255)
img.save("third_new.jpg")           
img.show()