from cv2 import *
import pyscreenshot as pys
import numpy as np
from collections import defaultdict
import keyboard as keyb
import time
image = pys.grab(bbox=(760,180,1270,680))
blocklist = []
for y in xrange(0,500,125):
    rowimage = []
    for x in xrange(5,510,127):
        box=(x,y,x+127,y+125)
        rowimage.append(image.crop(box))
    blocklist.append(rowimage)
by_color = defaultdict(int)
input_mat_color = []
input_row_color =[]
for x in blocklist:
    for y in x:
        by_color = defaultdict(int)
        for pixel in y.getdata():
            by_color[pixel]+=1
        by_color_sorted=sorted(by_color.iteritems(), key=lambda (k, v):v, reverse =True)
        input_row_color.append(by_color_sorted[0][0])
    input_mat_color.append(input_row_color)
    input_row_color = []
print input_mat_color
color_to_number =defaultdict(int)
color_to_number[tuple((205, 193, 180))] = 0
color_to_number[tuple((238, 228, 218))]=2
color_to_number[tuple((237, 224, 200))]=4
color_to_number[tuple((242, 177, 121))]=8
color_to_number[tuple((245, 149, 99))]=16
color_to_number[tuple((246, 124, 95))]=32
color_to_number[tuple((246, 94, 59))]=64
color_to_number[tuple((237, 207, 114))]=128
color_to_number[tuple((237, 204, 97))]=256
color_to_number[tuple((237, 200, 80))]=512
color_to_number[tuple((237, 197, 63))]=1024
color_to_number[tuple((237, 194, 46))]=2048

input_mat =[]
for each_row in input_mat_color:
    input_mat_row = []
    for each in each_row:
        input_mat_row.append(color_to_number[each])
    input_mat.append(input_mat_row)
    input_mat_row
print input_mat
keyb.wait('esc')

keyb.release('A')
keyb.release('S')
keyb.release('D')
keyb.press_and_release('W')
time.pause(.12)
image1 = pys.grab(bbox=(760,180,1270,680))

keyb.release('W')
keyb.release('S')
keyb.release('D')
keyb.press_and_release('A')
time.pause(.12)
image2 = pys.grab(bbox=(760,180,1270,680))

keyb.release('A')
keyb.release('W')
keyb.release('D')
keyb.press_and_release('S')
time.paue(.12)
image3 = pys.grab(bbox=(760,180,1270,680))

keyb.release('A')
keyb.release('S')
keyb.release('W')
keyb.press_and_release('D')
image1.show()
image2.show()
image3.show()
