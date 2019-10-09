# Import Needed Packages
import numpy as np
import cv2


# Create Black Image And Window
windowName = "Drawing"
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)

# True If Mouse Pressed
drawing = False

# If True, Draw Rectangle
# Press 'm' To Toggle
mode = True

# Set Initial Position
(ix,iy) = (-1,-1)


# Mouse Callback Function
def draw(event, x, y, flags, param):
	global ix, iy, drawing, mode
	
	# If L Mouse Button Pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		# Start Drawing
		# Update Initial Position
		drawing = True
		(ix,iy) = x,y
		
	# If Mouse Moving
	elif event == cv2.EVENT_MOUSEMOVE:
		# And Drawing Enabled (Clicked)
		if drawing == True:
			# If Mode Is Enabled, Draw Rectangle
			if mode == True:
				cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
			# Otherwise, Draw Circle
			else:
				cv2.circle(img, (x,y), 5, (0,0,255), -1)

	# Once L Mouse Button Released
	elif event == cv2.EVENT_LBUTTONUP:
		# Stop Drawing
		drawing = False
		
		
		
# Bind Callback Function To Window
cv2.setMouseCallback(windowName, draw)

def main():
	global mode, img
	
	while(True):
		# Display Window
		cv2.imshow(windowName, img)
	
		# Define Keypress Listener
		k = cv2.waitKey(1) & 0xFF
		
		# If 'm'/'M': Switch Modes
		if k == ord('m') or k == ord('M'):
			mode = not mode
		
		# If 'c'/'C': Clear Screen
		if k == ord('c') or k == ord('C'):
			img = np.zeros((512, 512, 3), np.uint8)
		
		# If 'ESC': Exit
		if k == 27:
			break

	# Cleanup
	cv2.destroyAllWindows()
		
		
if __name__ == "__main__":
	main()