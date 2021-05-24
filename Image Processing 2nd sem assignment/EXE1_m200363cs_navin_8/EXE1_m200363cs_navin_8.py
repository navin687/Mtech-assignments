# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:52:42 2021

@author: nkd
"""

from PIL import Image
import math

img= Image.open("C:/Users/nkd/Documents/python/question 3/third.jpg")
img = img.resize([64,64])
#img.show()
for i in range(64):
    for j in range(64):
       val=abs(math.cos(int(math.sqrt((i*i)+(j*j)))))
       newval=round(val,2)
       #print((newval))
       if newval>=0 and newval<0.25:
           img.putpixel((i,j),int(0*255))
       elif newval>=0.25 and newval<0.50:
           img.putpixel((i,j),int(0.25*255))
       elif newval>=0.5 and newval<0.75:
           img.putpixel((i,j),int(0.5*255))
       elif newval>=0.75 and newval<1:
           img.putpixel((i,j),int(0.75*255))
       else:
           img.putpixel((i,j),int(1*255))
           
img.save("third_new.jpg")
img.show()
  