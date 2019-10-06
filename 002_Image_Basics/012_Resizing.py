# Import Needed Packages
import cv2


# Load And Display Image
image = cv2.imread("../images/flowers.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# Define Aspect Ratio Of Desired Width To Current Width
# Resize Image To 500px Using Aspect Ratio
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0]*r))

# Resize Image (Width) And Display
# Interpolation Possibilities:
# INTER_AREA, INTER_LINEAR, INTER_CUBIC
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()