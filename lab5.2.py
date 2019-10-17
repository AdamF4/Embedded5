import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

stream=io.BytesIO()
with picamera.PiCamera() as camera:
	camera.resolution=(320,240)
	camera.framerate=24
	time.sleep(1)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)

window_name = 'lab 5.2'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

for x in range (0,240):
	for y in range (0,320):
		r,g,b=rgb[x,y]
		#r,g,b=image[x,y]
		if r>g and r>b and r>128:
			#image[x,y]=255,0,0
			rgb[x,y]=255,0,0


window_name2 = 'lab 5.2 red filter'
cv2.imshow(window_name2, rgb)
raw_key = cv2.waitKey(20000)
