# Import Needed Packages
import cv2


# Load Image, Convert Grayscale To Reduce Dimensions
image = cv2.imread("../images/white_square.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Note: 
# Better Accuracy Can Be Obtain With Binary Images
# Apply Thresholding Or Canny Edge Detector
edges = cv2.Canny(gray, 127, 255)
cv2.imshow("Edges", edges)

contours, heirarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Chain_Approx_None: All Boundary Points, Wherein Chain_Approx_Simple Gives Endpoints
# Saving Memory And Processing

# Print How Many Contours Were Found
print("Number Of Contours found: " + str(len(contours))) 

# Draw Contours And Display
# Contours Are Drawn On Image, Create Copy
drawnCnts = cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 

# Display Images
cv2.imshow("Original", image)
cv2.imshow("Contours", drawnCnts)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()

# For Further On The Topic, Please Consider The Following Tutorials:
# Sorting Contours...
# https://www.pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv/
# Removing Contours...
# https://www.pyimagesearch.com/2015/02/09/removing-contours-image-using-python-opencv/
# Find Extreme Contours...
# https://www.pyimagesearch.com/2016/04/11/finding-extreme-points-in-contours-with-opencv/
