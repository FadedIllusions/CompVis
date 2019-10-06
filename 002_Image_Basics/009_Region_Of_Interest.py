# Crop Region Of Interest (ROI)
#650x300

# Import Needed Packages
import numpy as np
import cv2


# Load Image
image = cv2.imread("../images/basketball.jpg")

# Display Original Image
cv2.imshow("Original", image)
cv2.waitKey(0)

# Select ROI
# 
roi = image[305:690, 650:1030]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()