# We Are Going To Create A BGR Color Picker
# Using Trackbars Within OpenCV

# Import Needed Packages
import numpy as np
import cv2


def emptyFunction(pos):
	pass 


def main():
	# Create Black Image, 512 x 512 px
	img = np.zeros((512, 512, 3), np.uint8)
	
	# Define Window Name And Create Future Window
	windowName = "OpenCV BGR Color Palette"
	cv2.namedWindow(windowName)
	
	# Create Trackbars
	# createTrackbar(name, windowName, startingPos, endingPos, functionToCall)
	cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
	cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
	cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)
	
	while(True):
		# Display Window
		cv2.imshow(windowName, img)
		
		blue = cv2.getTrackbarPos('B', windowName)
		green = cv2.getTrackbarPos('G', windowName)
		red = cv2.getTrackbarPos('R', windowName)
		
		# Crrete Composite Image
		img[:] = [blue, green, red]
				
		# Create Keypress Listener
		# If 'ESC': Exit
		k = cv2.waitKey(1) & 0xff
		if k == 27:
			break
			
	# Cleaup
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()