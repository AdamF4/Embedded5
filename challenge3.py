import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io


def make_circle(img,center,radius,color):
	for x in range(0,320):
		for y in range(0,240):
			if ((x-center[0])**2+(y-center[1])**2)<radius^2:
				img[x,y]=color
	return img

def sobel(img):
	img2=img

	height,width,channels=img.shape
	for x in range (1,height-1):
		for y in range (1,width-1):
			Gx=0
			Gy=0
			r,g,b=img[x-1,y-1]
			int=(r+g+b)
			Gx+=-int
			Gy+=-int
			r,g,b=img[x-1,y]
			Gx+=-2*(r+g+b)
			r,g,b=img[x-1,y+1]
			Gx+=-(r+g+b)
			Gy+=(r+g+b)
			r,g,b=img[x,y-1]
			Gy+=-2*(r+g+b)
			
			r,g,b=img[x,y+1]
			Gy+=-2*(r+g+b)
			
			r,g,b=img[x+1,y-1]
			Gx+=(r+g+b)
			Gy+=-(r+g+b)
			r,g,b=img[x+1,y]
			Gx+=2*(r+g+b)
			r,g,b=img[x+1,y+1]
			Gx+=(r+g+b)
			Gy+=(r+g+b)
			length=math.sqrt((Gx*Gx)+(Gy*Gy))
			length=length/4328*255
			length=numpy.floor(length)
			img2[x,y]=length,length,length
	return img2

stream=io.BytesIO()
with picamera.PiCamera() as camera:
	camera.resolution=(320,240)
	camera.framerate=24
	time.sleep(1)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)

window_name = 'challenge 3'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

image2=make_circle(rgb,[100,100],10,[255,199,100])


window_name2 = 'challenge 3 circle'
cv2.imshow(window_name2, image2)
raw_key = cv2.waitKey(5000)

image3=sobel(image2)


window_name2 = 'challenge 3 sobel'
cv2.imshow(window_name2, image3)
raw_key = cv2.waitKey(5000)
