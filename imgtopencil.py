import cv2
#Reading the image
vincent=cv2.imread('anna.jpg')

#Resizing image
width = int(vincent.shape[1] * 1/5)
height = int(vincent.shape[0] * 1/5)
dimensions = (width, height)
resized = cv2.resize(vincent, dimensions, interpolation = cv2.INTER_AREA)
cv2.imshow('Orignal',resized)

#Converting image to gray
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

#inverting gray image
inverted = 255 - gray
#cv2.imshow('Negetive',inverted)

#Applying gaussian blur to the inverted image
blur = cv2.GaussianBlur(inverted,(9,9),0)
#cv2.imshow('Negetive Blurred',blur)

#Inverting blurred image
invert_blur=255 - blur
pencil_sketch = cv2.divide(gray, invert_blur, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)

cv2.waitKey(0)