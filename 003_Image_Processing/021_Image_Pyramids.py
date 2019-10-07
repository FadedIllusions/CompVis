# Import Needed Packages
import numpy as np
import cv2

# Load Image
image = cv2.imread("../images/basketball.jpg")

# Generate Guassian Image Pyramid
copy = image.copy()
guassPyr = [copy]
count = 0

for i in range(4):
	cv2.imshow("Layer {}:".format(count+1), guassPyr[count])
	copy = cv2.pyrDown(copy)
	guassPyr.append(copy)
	count += 1

cv2.imshow("Layer: {}".format(count+1), guassPyr[count])
cv2.waitKey(0)

cv2.destroyAllWindows()