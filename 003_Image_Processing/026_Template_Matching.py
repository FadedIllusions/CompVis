# Template Matching Is Used To Find A Template Image Within A Larger Image
# A Bit Like Finding Waldo In "Where's Waldo?"

# Import Needed Packages
import matplotlib.pyplot as plt
import cv2

# Load Image And Load Template
template = cv2.imread("../images/stars_template.jpg", 0)
image = cv2.imread("../images/stars.jpg", 0)

# Obtain Template Dimensions
w, h = template.shape[::-1]

# List Of Template Matching Methods For Comparison
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 
		   'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED',
		   'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED']

# Iterate Through Methods
for method in methods:
	copy = image.copy()
	method = eval(method)
	
	# Apply Template Matching
	result = cv2.matchTemplate(copy, template, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	
	# Get Coords For Rectangle
	# If Method Is TM_SQDIFF or TM_SQDIFF_NORMED, Use Min
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	
	# Draw Rectangle
	cv2.rectangle(copy, top_left, bottom_right, 0, 2)
	
	plt.subplot(121), plt.imshow(result, cmap='gray')
	plt.title("Matching"), plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(copy, cmap='gray')
	plt.title("Detection"), plt.xticks([]), plt.yticks([])
	plt.suptitle(method)
	
	plt.show()