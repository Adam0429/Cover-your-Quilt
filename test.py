import cv2
import numpy as np
import time
from time import strftime
import IPython

def mouseColor(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(str.upper(out), color[y, x])  #输出图像坐标(x,y)处的HSV的值

def alert(img):
	print('save image')
	cv2.imwrite("no_quilt.png",img)

cap = cv2.VideoCapture(0)

x = 664
y = 292
h = 200
w = 400
fps = cap.get(cv2.CAP_PROP_FPS)

detect_time = 10
color_len = detect_time * fps
quilt_color = 100
colors = [] 

print('Begin detect...')

while True:
	success,img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #变成灰度图
	# cv2.cvtColor(gray, cv2.COLOR_BGR2HSV)  #变成HSV格式
	cv2.putText(gray, strftime("%H:%M:%S"), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,255,0),2,cv2.LINE_AA)
	img = cv2.rectangle(gray, (x+w,y+h), (x,y), (255,255,255), 2)

	cv2.namedWindow("Color Picker")
	cv2.setMouseCallback("Color Picker", mouseColor)
	cv2.imshow("img",gray)

	color = img[y+2:y+h-2,x+2:x+w-2] # +2,-2 去掉白框,注意shape与img是倒的
	color_mean = color.mean()

	colors.append(color_mean)
	if len(colors) == color_len:
		print('light:',sum(colors)/color_len)
		if sum(colors)/color_len < quilt_color: 
			print(strftime("%H:%M:%S"),'No quilt')
			alert(img)
			time.sleep(2)
			break
		else:
			colors = []
			colors.append(color_mean)

	k = cv2.waitKey(1)
	if k == 27:
		#通过esc键退出摄像
		cv2.destroyAllWindows()
		break

