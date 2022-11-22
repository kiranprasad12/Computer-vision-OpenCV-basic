import cv2

img = cv2.imread('Asserts/0.jpg',0) #reading the image and using of grayscale
# -1 means reading of colour image, transprency neglected
#  0 means Grayscale of the image.
#  1 means reading of original image.
img = cv2.resize(img,(0,0), fx=0.5,fy=0.5) #resizing the image by using cv2.resize
img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE) #insted of using cv2.cv2.ROTATE_90_CLOCKWISE use cv2.ROTATE_90_CLOCKWISE
img = cv2.imwrite('the_new_image_0.jpg', img) # Saving the modified image
cv2.imshow('Image',img)
cv2.waitKey(0)
cv.destoryAllWindows()
