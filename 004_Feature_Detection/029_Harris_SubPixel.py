# Sometimes, You May Need To Locate Corners With Greater Precision

# Import Needed Packages
import numpy as np
import cv2

# Load Image, Convert To Grayscale
image = cv2.imread("../images/grid.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Corner Detection
gray = np.float32(gray)
# cornerHarris(image, blockSize, kSize, k)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate To Better Mark Corners
dst = cv2.dilate(dst, None)

# Threshold
ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
dst = np.uint8(dst)

# Find Centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# Define Criteria To Stop And Refine Corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5,5), (-1,-1),criteria)

# Draw
result = np.hstack((centroids, corners))
result = np.int0(result)
image[result[:,1], result[:,0]] = [0, 0, 255]
image[result[:,3], result[:,2]] = [0, 255, 0]

# Display Precise Corners
cv2.imshow("Precise Corners", image)
cv2.waitKey(0)

# Note:
# Have To Look Closely For The Red And Green Dots
# Red Dots Indicate Inside Of Corner
# Green Dots Indicate Outside Of Corner