# Import Needed Packages
import numpy as np
import cv2

# Load Image As Grayscale
image = cv2.imread("../images/low_contrast.jpg", 0)

# Equalize Image Histogram
equalized = cv2.equalizeHist(image)

# Display Images, Side-By-Side, For Comparison
# (Using Numpy's Horizongtal Stack Method)
result = np.hstack((image, equalized))
cv2.imshow("Equalization Comparison", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Consider A Really Dark Or Really Bright Image. Both Will Have A Histogram
# With Values Favoring One End Of The Specturm Or Another -- Bright Images 
# Favoring Bright Colors, Etc. Histogram Equalization, Essentially, 'Stretches'
# The Histogram To Better Equalize It Across The Entire Range, Thereby Often
# Improving The Overall Contrast Of The Image