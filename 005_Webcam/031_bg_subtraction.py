# Subtracts Non-Moving 'Background' Objects From Video,
# Showing Only Those Parts Of Image That Move
# Anti-Ninja Via Computer Vision? 

# Import Needed Packages
import numpy as np
import cv2


# Initialize Stream Object -- Onboard Webcam
stream = cv2.VideoCapture(0)

# Initialize Background Subtractor Object
fgbg = cv2.createBackgroundSubtractorMOG2()

# While There Is A Video Stream
while True:
	# Grab Frame
	_, frame = stream.read()
	
	# Apply Background Subtractor
	fgmask = fgbg.apply(frame)
	
	# Display Original And Masked Stream
	cv2.imshow("Video Stream", frame)
	cv2.imshow("FG Mask Stream", fgmask)
	
	# Capture Keypress
	# If Key 'ESC': Quit
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	

# Cleanup
stream.release()
cv2.destroyAllWindows()
