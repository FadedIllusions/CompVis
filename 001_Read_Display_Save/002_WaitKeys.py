# Press 'ESC' To Exit
# Press 's" To Save

# Import Needed Packages
import cv2


# Load Image
image = cv2.imread("../images/flowers.png")

# Display Image
cv2.imshow("Flowers", image)

# Capture Keypress
# If 'ESC', Exit
# If 's', Save Image Copy And Exit
key = cv2.waitKey(0)

if key == 27:
	cv2.destroyAllWindows()
elif key == ord('s'):
	cv2.imwrite("../images/flowers_copy.png", image)
	cv2.destroyAllWindows()