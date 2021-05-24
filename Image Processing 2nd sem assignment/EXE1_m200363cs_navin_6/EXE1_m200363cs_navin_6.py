from PIL import Image
try:

    grayimg = Image.open("C:/Users/nkd/Documents/python/sample1.jpg")
    img = grayimg.resize([256,256])
    input_pixels = img.load()
    img.save("new_sample1.jpg", "JPEG")
    #img.show()
    imin = 255
    imax = 0
    for x in range(img.width):
     for y in range(img.height):
        r, g, b = input_pixels[x, y]
        i = (r + g + b) / 3
        imin = min(imin, i)
        imax = max(imax, i)
      
       
    print("Maximum Intensity=" , int(imax))
    print("Minimum Intensity=" , int(imin))     
except IOError:
    pass



