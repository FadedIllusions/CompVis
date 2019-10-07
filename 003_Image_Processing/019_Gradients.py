# Import Needed Packages
import numpy as np
import cv2


# Load Image
image = cv2.imread("../images/basketball.jpg")

# For This Project, We're Interested Only In The Basketball;
# So, Let's Crop The Image To Contain Just The Basketball
# Saving The Basketball As A Separate Picture In Case Needed
# In The Future
basketball= image[305:690, 650:1030]
cv2.imwrite("../images/basketball_only.jpg", basketball)
cv2.imshow("Basketball", basketball)

# Convert Image To Grayscale
gray = cv2.cvtColor(basketball, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)


# Apply Laplacian, Display
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

# Apply Sobel, Display
sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()