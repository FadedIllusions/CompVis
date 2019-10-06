# Import Needed Packages
import numpy as np
import cv2


# Load Both Images
flowers = cv2.imread("../images/flowers.png")
logo = cv2.imread("../images/opencv_logo.png")


# Resize Logo
r = 200 / logo.shape[1]
dim = (200, int(logo.shape[0] * r))
logo = cv2.resize(logo, dim, interpolation=cv2.INTER_AREA)

# Display Images
cv2.imshow("Flowers", flowers)
cv2.imshow("Logo", logo)
cv2.waitKey(0)


# Define ROI (Within Which To Place Overlaid Image)
rows, cols, chans = logo.shape
roi = flowers[0:rows, 0:cols]

# Create Logo Mask And Invert
gray_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_logo, 150, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)


# Black-Out Area Of Logo In ROI
flowers_bg = cv2.bitwise_and(roi, roi, mask=mask)

# Take Only Region Of Logo From Logo Image
logo_fg = cv2.bitwise_and(logo, logo, mask=mask_inv)

# Place Logo In ROI
destination = cv2.add(flowers_bg, logo_fg)
flowers[0:rows, 0:cols] = destination


# Display Images In Horizontal Stack To Ensure The Both Loaded
cv2.imshow("Combined", flowers)
cv2.waitKey(0)