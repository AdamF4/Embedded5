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

window_name = 'lab 5.5'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

rgb[120,64]=0,128,255


window_name2 = 'lab 5.5 orange pixel'
cv2.imshow(window_name2, rgb)
raw_key = cv2.waitKey(20000)
