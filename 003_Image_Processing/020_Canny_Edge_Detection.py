# Import Needed Packages
import cv2

# Load Image; Then, Convert To Grayscale
image = cv2.imread("../images/basketball_only.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur Image To Reduce Noise
# Find Edges Using Canny
blur = cv2.GaussianBlur(gray, (3,3), 0)
edges = cv2.Canny(image, 0, 150)

# Display Images
cv2.imshow("Original", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()