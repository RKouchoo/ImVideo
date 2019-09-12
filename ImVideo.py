import cv2
import numpy as np
import glob

frame_delay = 15
path = '/raw_images'
name = 'latest_timelapse.avi'

img_array = []

for filename in glob.glob(path):
    
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
 
 
out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'DIVX'), frame_delay, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])

out.release()