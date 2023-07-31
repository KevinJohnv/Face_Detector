import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Image being used to detect face
img = cv2.imread('MR.jpg')

# Gray scale the image
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


# Draw rectangle around the face
(x,y, w, h) = face_coordinates[0]
cv2.rectangle((img),(x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Kevin's Face Detector",img)
cv2.waitKey()


print("Code Completed")