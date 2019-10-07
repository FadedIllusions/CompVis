# Import Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import cv2


# Load Image As Grayscale
image = cv2.imread("../images/receipt.jpg", 0)
#cv2.imshow("Original", image)

# Notice The Original Image Is Sideways;
# So, Let's Rotate It
# We'll, Also, Resize It A Bit

# Define Aspect Ratio Of Desired Width
# Resize To 500 Px Using Aspect Ratio
r = 750.0 /image.shape[1]
dim = (750, int(image.shape[0]*r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)

# Get Image Dimensions And Center Point
(h, w) = resized.shape[:2]
center = (w//2, h//2)

# Create Rotational Matrix
# Rotate 90 Degrees CCW
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(resized, M, (w,h))
cv2.imshow("Original - Rotated", rotated)

# Blur Image To Remove Noise
blurred = cv2.medianBlur(rotated, 3)
cv2.imshow("Median Blur", blurred)

# Threshold Image -- Global Thresholding
_, thresh_global = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Global Threshold", thresh_global)

# Threshold Image -- Adaptive Mean Thresholding
thresh_mean = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Adaptive Mean", thresh_mean)

# Threshold Image -- Adaptive Guassian Thresholding
thresh_gauss = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Adaptive Gaussian", thresh_gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()