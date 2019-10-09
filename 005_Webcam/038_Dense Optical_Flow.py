# Unlike Lucas-Kanade, Colors Are Used To Reflect Movement With Hue 
# Being Direction And Value (Brightness/Intensity) Being Speed

# Import Needed Packages
import numpy as np
import cv2

# Init Video Stream
cap = cv2.VideoCapture(0)

# Grab Frame
_, first_frame = cap.read()
previous_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(first_frame)
hsv[...,1] = 255

while True:
	# Grab Frame
	_, frame2 = cap.read()
	next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
	
	# Computes Dense Optical Flow Using Gunnar Forneback's Algorithm
	flow = cv2.calcOpticalFlowFarneback(previous_gray, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	
	# Use Flow To Calculate The Magnitude (Speed) And Angle Of Motion
	# Use These Values To Calculate The Color To Reflect Speed And Angle
	magnitude, angle = cv2.cartToPolar(flow[...,0], flow[...,1])
	hsv[...,0] = angle * (180/ (np.pi/2))
	hsv[...,2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
	final = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	
	# Show Dense Optical Flow
	cv2.imshow("Dense Optical Flow", final)
	
	# Define Key Listener
	k = cv2.waitKey(1) & 0xFF;
	if k == 27:
		break
		
	# Store Current Image As Previous Image
	previous_gray = next
	
	
# Cleanup
cap.release()
cv2.destroyAllWindows()