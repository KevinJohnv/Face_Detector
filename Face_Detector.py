import cv2


"""""
###########################################################
#This sections iwll take in a image and report the face s is finds
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Image being used to detect face
img = cv2.imread('MR.jpg')

# Gray scale the image
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


# Draw rectangle around the face
#(x,y, w, h) = face_coordinates[0]

# Loops through all faces that have been found and start to draw boxes around them
for (x,y,w,h) in face_coordinates:
    cv2.rectangle((img),(x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Kevin's Face Detector",img)
cv2.waitKey()
"""
###########################################################

###########################################################
# Algorithim to detect faces
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture webcam
webcam = cv2.VideoCapture(0)

# Go through all of the frames forever
while True:
    # Get frame
    successful_frame_read, frame = webcam.read()

    # Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangle around the face
    # (x,y, w, h) = face_coordinates[0]

    # Loops through all faces that have been found and start to draw boxes around them
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle((frame), (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Kevin's Face Detector",frame)
    key = cv2.waitKey(1)

    if key==81 or key == 113:
        webcam.release()
        break







print("Code Completed")