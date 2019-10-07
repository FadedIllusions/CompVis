# Features From Accelerated Segment Test

# Import Needed Packages
import cv2

# Load Image As Grayscale, Display
image = cv2.imread("../images/hand.png", 0)
copy = image.copy()
copy2 = image.copy()
cv2.imshow("Original", image)
cv2.waitKey(0)

# Init FAST Object
fast = cv2.FastFeatureDetector_create()

# Find And Draw Keypoints
kp = fast.detect(image, None)
copy = cv2.drawKeypoints(image, kp, copy, color=(255,0,0))

# Display NonMaxSuppression Image
cv2.imshow("With NonMaxSuppression", copy)
cv2.waitKey(0)