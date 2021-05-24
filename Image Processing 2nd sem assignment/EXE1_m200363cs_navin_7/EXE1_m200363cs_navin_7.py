# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:36:11 2021

@author: nkd
"""

from PIL import Image
import math


img = Image.new("L",[64,64]) 
#img.show()
for i in range(64):
    for j in range(64):
       find = abs(math.cos(int(math.sqrt((i*i)+(j*j)))))
       #print(round(find, 1))
       img.putpixel((i,j),int(find))
      
img.save("second_new.jpg")       
img.show() 