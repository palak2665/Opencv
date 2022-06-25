import cv2
path = 'resources/faces.png'

facecascade = cv2.CascadeClassifier('resources/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread(path)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(imggray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result", img)
cv2.waitKey(0)


