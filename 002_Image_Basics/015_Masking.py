# Import Needed Packages
import numpy as np
import cv2


# Load And Display Image
image = cv2.imread("../images/basketball.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

# Create Mask, Find Image Center, Determine ROI, Show Mask
mask = np.zeros(image.shape[:2], dtype="uint8")
(centerX, centerY) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (centerX+89, centerY-67), (centerX+465, centerY+315), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

# Mask And Display Image
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()