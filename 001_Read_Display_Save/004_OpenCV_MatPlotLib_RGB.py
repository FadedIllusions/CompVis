# Import Needed Packages
import matplotlib.pyplot as plt
import cv2

# Load Image
image = cv2.imread("../images/flowers.png")

# Plot Image With MatPlotLib
# Note That OpenCV Loads Images In BGR Format
# Wherein MPL Uses RGB
plt.imshow(image)
plt.xticks([]), plt.yticks([])
plt.show()

# To Rectify The Channel Discrepancy,
# You Can Use One Of The Following Two Ways

# Reverse Channels
image2 = image[:,:,::-1]
plt.imshow(image2)
plt.xticks([]), plt.yticks([])
plt.show()

# Reverse Channels Via OpenCV
image3 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image3)
plt.xticks([]), plt.yticks([])
plt.show()