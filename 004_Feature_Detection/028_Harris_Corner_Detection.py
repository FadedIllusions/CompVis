# Import Needed Packages
import numpy as np
import cv2

# Load Image, Convert To Grayscale
image = cv2.imread("../images/grid.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Corner Detection
gray = np.float32(gray)
# cornerHarris(image, blockSize, kSize, k)
result = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate To Better Mark Corners
result = cv2.dilate(result, None)

# Threshold For Optimal Value
image[result > 0.01 * result.max()] = [0, 0, 255]

# Display Detected Corners
cv2.imshow("Detected Corners", image)
cv2.waitKey(0)