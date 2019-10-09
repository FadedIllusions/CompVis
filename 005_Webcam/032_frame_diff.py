# Import Needed Packages
import cv2


# Compares Differences Between Frames
# Much Like webcam_bgSubtraction.py, Can Be Used With Object Tracking Or Motion Detections

# Compute Frame Differences
def frame_diff(prev_frame, cur_frame, next_frame):
	# Diffence Between Current Frame And Next Frame
	diff_frames_1 = cv2.absdiff(next_frame, cur_frame)
	
	# Difference Between Current Frame And Previous
	diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)
	
	return cv2.bitwise_and(diff_frames_1, diff_frames_2)
	
	
# Defines Function To Get Current Frame
def get_frame(cap, scaling_factor):
	# Read Current Frame From Video Capture Object
	_, frame = cap.read()
	
	# Resize Image
	frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
	
	# Convert To Grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	return gray


if __name__ == '__main__':
	# Init Video Capture Object
	cap = cv2.VideoCapture(0)
	
	# Define Scaling Factor
	scaling_factor = 1.5
	
	# Grab Current Frame, Next, And Following
	prev_frame = get_frame(cap, scaling_factor)
	cur_frame = get_frame(cap, scaling_factor)
	next_frame = get_frame(cap, scaling_factor)
	
	# While Video Stream Open
	while True:
		# Display Frame Difference
		cv2.imshow("Object Movement", frame_diff(prev_frame, cur_frame, next_frame))
		
		# Update Frame Variables
		prev_frame = cur_frame
		cur_frame = next_frame
		next_frame = get_frame(cap, scaling_factor)
		
		# Listen For Keypress
		# If 'ESC': Exit
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
			
			
# Cleanup
cap.release()
cv2.destroyAllWindows()