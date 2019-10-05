# Import Needed Packages
import matplotlib.pyplot as plt
import cv2

# Read Image In As Grayscale
image = cv2.imread("../images/flowers.png", 0)

# Plot Image With MatPlotLib, Hiding Tick Values
plt.imshow(image, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])
plt.show()