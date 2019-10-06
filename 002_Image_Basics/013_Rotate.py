# Import Needed Packages
import cv2


# Load And Display Image
image = cv2.imread("../images/flowers.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# Get Image Dimensions And Centerpoint
(h, w) = image.shape[:2]
center = (w//2, h//2)

# Create Rotational Matrix
# From Center Point, Rotate 45 Degrees CCW With Scale Of 100%
# (Use Negative For CW)
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# Rotate Image And Display
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)