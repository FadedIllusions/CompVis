# CLAHE (Contrast Limited Adaptive Histogram Equalization)

# Import Needed Packages
import numpy as np
import cv2


# Load Image As Grayscale
image = cv2.imread("../images/low_contrast.jpg", 0)

# Create CLAHE Object
clahe = cv2.createCLAHE()
image_clahe = clahe.apply(image)

# Display Images, Side-By-Side, For Comparison
result = np.hstack((image, image_clahe))
cv2.imshow("Equalization Comparison", result)
cv2.waitKey(0)
cv2.destroyAllWindows()