# Slight Variation Of Previous File 031_bg_subtraction.py
# Suggested To Start Script Without Moving Objects In Front Of BG;
# But, Not Mandatory

# Import Needed Packages
import numpy as np
import cv2


# Define Function TO Get Current Frame
def get_frame(cap, scaling_factor):
	# Read Current Frame From Video Capture Object
	_, frame = cap.read()
	
	# Resize Frame
	frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
	
	return frame


if __name__ == '__main__':
	# Init Video Capture Object
	cap = cv2.VideoCapture(0)
	
	# Define Background Subtractor Object
	bg_subtractor = cv2.createBackgroundSubtractorMOG2()
	
	# Define Number Of Previous Frames To Use To 'Learn'. Higher Value Creating
	# A Slower Learning Rate. Modify Value As Desired. Experiment.
	history = 100
	
	# Define Learning Rate
	learning_rate = 1.0 / history
	
	# While Streaming
	while True:
		# Grab Frame
		frame = get_frame(cap, 1.0)
		
		# Compute Mask, Convert To RGB
		mask = bg_subtractor.apply(frame, learningRate=learning_rate)
		mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
		
		# Display Images
		cv2.imshow("Original Stream", frame)
		cv2.imshow("Detection Stream", mask & frame)
		
		# Listen For Keypress
		# If 'ESC': Exit
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
			
			
# Cleanup
cap.release()
cv2.destroyAllWindows()