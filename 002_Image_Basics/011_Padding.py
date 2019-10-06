# Import Needed Packages
from matplotlib import pyplot as plt
import numpy as np
import cv2

# Load Image, Convert To RGB
image = cv2.imread("../images/opencv_logo.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create Boareded Images
replicate = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT)

# Plot Subplots To Display Images Together
plt.subplot(231),plt.imshow(image,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT 101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

# Display Plot
plt.show()