# Import Needed Packages
import matplotlib.pyplot as plt
import cv2


# Load And Display Image
image = cv2.imread("../images/nature.jpg")
cv2.imshow("Original", image)

# Iterate Through Color Channels
# And Plot On Single Histogram
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
	# calcHist(image, channels, mask, histSize, range)
	hist = cv2.calcHist([image], [i], None, [256], [0, 256])
	plt.plot(hist, color = color)
	plt.xlim([0, 256])
plt.show()

# The Histogram Size (Number Of Bins) Represent The Value Of Pixels 
# You Wish To Calculate. In Our Example, We're Displaying The Full
# Range, From 0 - 256; Though, You Could Just As Easily Calculate
# The Range Of Pixel Values Between 0 And 15, If So Desired.