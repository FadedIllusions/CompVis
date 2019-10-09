# Import Needed Packages
import numpy as np
import time
import cv2

def main():
	# Init Video Stream
	cap = cv2.VideoCapture(0)
	
	# Get Single Frame So As To Read In Dimensions
	_, frame = cap.read()
	rows, columns, channels = frame.shape
	
	# Find Image Center
	center = (columns/2, rows/2)
	
	
	# Define Initial Angle
	angle = 0
	
	while True:
		# Get Frame
		_, frame = cap.read()
		
		# Reset Angle Variable, If Needed
		if angle == 360:
			angle = 0
			
		# Define Rotational Matrix And Apply
		R = cv2.getRotationMatrix2D(center, angle, 0.75)
		rotated = cv2.warpAffine(frame, R, (columns, rows))
		
		# Display Rotating Stream
		cv2.imshow("Rotating Live Stream", rotated)
		
		# Update Angle
		angle += 1
		
		# Define Keypress Listener
		# If 'ESC': Exit
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
		
		# Create Slight Pause Between Iterations
		# Adjust To Slow/Speed Rotation
		time.sleep(0.0)
		
	# Cleanup
	cap.release()
	cv2.destroyAllWindows()
	
	
	
if __name__ == '__main__':
	main()