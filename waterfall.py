# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:58:15 2017

@author: zhai14
"""
import operator
import numpy
from PIL import Image,ImageDraw
image = Image.open('2.jpg')

print image.size
image.thumbnail((300, 300))
l,h = image.size
print (l,h)

x = 0
y = 0
end2 = 1
side1 = [0]*l
i = 0
min_l1 = [0]*(h+1)
max_l1 = [0]*(h+1)

def findmode(values):  
    bucket = {}  
    for value in values:  
        if bucket.has_key(value):  
            bucket[value] += 1  
        else:  
            bucket.setdefault(value,1)  
    bucket = sorted(bucket.iteritems(),key=operator.itemgetter(1),reverse=True)  
      
    modes  = []  
    for value in bucket:  
        if len(modes) == 0:  
            modes.append(value)  
        else:  
            temp = modes[len(modes)-1][1]  
            if temp == value[1]:  
                modes.append(value)  
            else:  
                break  
    return modes 

while y<h-1:
    y = y + 1
    x = 0
    while x <= l-1:
#   while y <= h:# Fill in the condition (before the colon) 
        r,g,b = image.getpixel((x,y)) 
        if (r>220 and g>220 and b>220):
            side1[x]= x        
        x = x + 1

    l1 = list(set(side1))

    if (l1 == [0]):
        min_l1 [i] = 0 
        max_l1 [i] = 0
    else:    

        del l1[0]

        min_l1 [i] = min(l1) 
        max_l1 [i] = max(l1)
    i = i + 1
    #print(i)
       





modes1 = findmode(min_l1)
modes2 = findmode(max_l1)

print(modes1[0][0])
print(modes2[0][0])

side_v1 = modes1[0][0]
side_v2 = modes2[0][0]



draw_instance = ImageDraw.Draw(image)

draw_instance.line([modes1[0][0], 0, modes1[0][0], l],fill = (255, 100, 0), width = 3)
draw_instance.line([modes2[0][0], 0, modes2[0][0], h],fill = (255, 0, 0), width = 3)
del draw_instance

image.show()
image.save('2_.jpg')
