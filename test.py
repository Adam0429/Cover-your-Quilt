import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def mouseColor(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(str.upper(out), color[y, x])  #输出图像坐标(x,y)处的HSV的值

while True:
	#从摄像头读取图片
	sucess,img=cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #变成灰度图
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #变成HSV格式
	out = 'bgr'
	color = img[1][700]
	if color[0] >100 and color[1]>100 and color[2]>100:
		print('人物在检测区域')
	else:
		print('人不在')
	# out = 'gray'
	# color = gray
	# out == 'hsv':
	# color = hsv
	cv2.namedWindow("Color Picker")
	cv2.setMouseCallback("Color Picker", mouseColor)
	#转为灰度图片
	#显示摄像头，背景是灰度。
	cv2.imshow("img",gray)
	#保持画面的持续。
	k=cv2.waitKey(1)
	if k == 27:
		#通过esc键退出摄像
		cv2.destroyAllWindows()
		break
	elif k==ord("s"):
		#通过s键保存图片，并退出。
		cv2.imwrite("image2.jpg",img)
		cv2.destroyAllWindows()



# img_BGR = cv2.imread('citrus-fruit-colorful-delicious-2146386.jpg') 
# print(type(img_BGR)) # numpy.ndarray类型可以用numpy对图像进行各种操作
# print(img_BGR.dtype) # 图像数据类型，一张图片的像素值范围是[0,255], 因此默认类型是unit8
# print(img_BGR.shape[0]) # 行
# print(img_BGR.shape[1]) # 列
# print(img_BGR.shape[2]) # 通道
# print(img_BGR.size) # 像素数目
# print(img_BGR.max()) # 最大像素值
# print(img_BGR.min()) # 最小像素值
# print(img_BGR.mean()) #素值平均值

# # 定义鼠标交互函数
# def mouseColor(event, x, y, flags, param):
#	 if event == cv2.EVENT_LBUTTONDOWN:
#		 print(str.upper(out), color[y, x])  #输出图像坐标(x,y)处的HSV的值

# img = cv2.imread('3.PNG')  #读进来是BGR格式
# # 进行颜色格式的转换
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #变成灰度图
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #变成HSV格式
# out = 'bgr'
# color = img
# # out = 'gray'
# # color = gray
# # out == 'hsv':
# #	 color = hsv
# cv2.namedWindow("Color Picker")
# cv2.setMouseCallback("Color Picker", mouseColor)
# cv2.imshow("Color Picker", img)
# if cv2.waitKey(0):
#	 cv2.destroyAllWindows()
