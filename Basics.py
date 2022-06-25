import cv2
import numpy as np

#image_show

# img = cv2.imread('E:\\Artificial Intelligence\\OpenCV\\resources\\lena.png')

# cv2.imshow("output",img)
# cv2.waitKey(0)

#video_capture

# cap = cv2.VideoCapture("E:\\Artificial Intelligence\\OpenCV\\resources\\earth.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#webcam

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

# while True:
#     success, img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#Basic Functions

# img = cv2.imread("resources/lena.png")
# kernel = np.ones((5,5),np.uint8)

# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img, (7,7), 0)
# imgCanny = cv2.Canny(img,150,200)
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

# cv2.imshow("gray image",imgGray)
# cv2.imshow("blur image",imgBlur)
# cv2.imshow("canny image",imgCanny)
# cv2.imshow("image Dialation",imgDialation)
# cv2.imshow("blur image",imgEroded)
# cv2.waitKey(0)

# resize n crop

# img = cv2.imread('resources/lambo.png')
# print(img.shape)

# imgresize = cv2.resize(img,(300,200))

# imgcropped = img[0:200,200:500]

# cv2.imshow('lambo',img)
# cv2.imshow('resize',imgresize)
# cv2.imshow('cropped',imgcropped)


# cv2.waitKey(0)

#shapes n text

# img = np.zeros((512,512,3))
# #img[:] = 255,0,0

# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),1)
# cv2.circle(img,(400,50),30,(255,255,0),cv2.FILLED)
# cv2.putText(img," Hello World! ",(300,100),cv2.FONT_ITALIC,1,(0,150,0),1)

# cv2.imshow('image',img)

# cv2.waitKey(0)

#wrap perspective


# img = cv2.imread('resources/cards.jpg')

# width, height = 250,350

# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))

# cv2.imshow('image', imgOutput)

# cv2.waitKey(0)

#joining images

# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
 
# img = cv2.imread('Resources/lena.png')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))
 
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
# cv2.imshow("ImageStack",imgStack)
 
# cv2.waitKey(0)

