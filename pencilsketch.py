import cv2
import sys

pic = input("Set the Directory to the Image: ")
image = cv2.imread(pic)

grayImage = cv2.cvtColor(image, cv2.COLOR_BRG2GRAY)
grayImage = 255 - grayImage

grayImageInv = cv2.gaussianBlur(grayImageInv, (21, 21), 0)

output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)

cv2.namedWindow("Image", cv2.WINDOWS_AUTOSIZE)
cv2.namedWindow("Pencilsketch", cv2.WINDOWS_AUTOSIZE)

cv2.imshow("Image", image)
cv2.imshow("Pencilsketch", output)
cv2.waitKey(0)
cv2.destroyAllWindows()