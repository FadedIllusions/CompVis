# Import Needed Packages
import cv2

# Load Image In Grayscale
# cv2.IMREAD_COLOR()       =>   cv2.imread("image.png", 1)
# cv2.IMREAD_GRAYSCALE()   =>   cv2.imread("image.png", 0)
# cv2.IMREAD_UNCHANGED()   =>   cv2.imread("image.png", -1)
image = cv2.imread("../images/flowers.png", 0)

# Display Image In Premade, Resizable Window
# Could, Also, Create A Premade, Auto-Sizing Window:
# cv2.namedWindow("Auto-Size", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Resizable", cv2.WINDOW_NORMAL)
cv2.imshow("Resizable", image)
cv2.waitKey(0)

# Save Window
# (Saves As Grayscale, As It Was Loaded)
cv2.imwrite("../images/flowers_grayscale.png", image)

# Destroy Specific Window (By Name)
cv2.destroyWindow("Resizable")
