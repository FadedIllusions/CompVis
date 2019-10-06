# Import Needed Packages
import numpy as np
import cv2


# Load Image
image = cv2.imread("../images/basketball.jpg")

# Split Channels
# b = image[:,:,0]
# g = image[:,:,1]
# r = image[:,:,2]
b, g, r = cv2.split(image)

# Merge Channels
merged = cv2.merge((b,g,r))

# Can Fill Channel Without Splitting
# merged[:,:,2] = 0

# Display Images
cv2.imshow("Original", image)
cv2.imshow("B-Channel", b)
cv2.imshow("Merged", merged)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()

# cv2.split() is More Computationally Expensive Than Numpy Indexing