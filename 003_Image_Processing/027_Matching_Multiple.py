# Import Needed Packages
import numpy as np
import cv2

# Load Image, Copy, Convert To Grayscale, Load Template (As Grayscale)
template = cv2.imread("../images/stars_template_002.jpg", 0)
image = cv2.imread("../images/stars_002.jpg")
copy = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Grab Dimensions Of Template
w, h = template.shape[::-1]

# Match Template, Create And Apply Threshold For Matching
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result>=threshold)

# Iterate Through Threshold Matches
for pt in zip(*loc[::-1]):
	# Draw Rectangle On Match
	cv2.rectangle(copy, pt, (pt[0] +w, pt[1] +h), (0, 0, 255), 1)
	
# Display Matches
cv2.imshow("Original", image)
cv2.imshow("Result", copy)
cv2.waitKey(0)
cv2.destroyAllWindows()