# Import Needed Packages
import numpy as np
import cv2


# Define Function To Track Object
def start_tracking():
	# Init Video Capture Device
	cap = cv2.VideoCapture(0)
	
	# Define Scaling Factor
	scaling_factor = 1.0
	
	# Number Of Frames To Track
	num_frames_to_track = 5
	
	# Skipping Factor
	num_frames_jump = 2
	
	# Initialize Variables
	tracking_paths = []
	frame_index = 0
	
	# Define Tracking Parameters
	tracking_params = dict(winSize=(11,11), maxLevel=2, 
						   criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
	
	# While Streaming
	while True:
		# Grab Frame
		_, frame = cap.read()
		
		# Resize Frame
		frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,
						   interpolation=cv2.INTER_AREA)
		
		# Covert To Grayscale
		frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		# Copy Frame
		output_img = frame.copy()
		
		if len(tracking_paths) > 0:
			# Get Images
			prev_img, current_img = prev_gray, frame_gray
			
			# Organize Feature Points
			feature_points_0 = np.float32([tp[-1] for tp in tracking_paths]).reshape(-1,1,2)
			
			# Compute Optical Flow
			feature_points_1, _, _ = cv2.calcOpticalFlowPyrLK(prev_img, current_img, feature_points_0,
															  None, **tracking_params)
			
			# Compute Reverse Optical Flow
			feature_points_0_rev, _, _ = cv2.calcOpticalFlowPyrLK(current_img, prev_img, feature_points_1,
																  None, **tracking_params)
			
			# Compute Difference Between Forward And Reverse Optical Flow
			diff_feature_points = abs(feature_points_0 - feature_points_0_rev).reshape(-1,2).max(-1)
			
			# Extract Good Points
			good_points = diff_feature_points < 1
			
			# Initialize Variable
			new_tracking_paths = []
			
			# Iterate Over Good Feature Points
			for tp, (x,y), good_points_flag in zip(tracking_paths, feature_points_1.reshape(-1,2),
												   good_points):
				
				# If Flag Not True, Continue
				if not good_points_flag:
					continue
					
				# Append (x,y) Coordinates And Check If Length Greater Than Threshold
				tp.append((x,y))
				if len(tp) > num_frames_to_track:
					del tp[0]
					
				new_tracking_paths.append(tp)
				
				# Draw Circle Around Feature Points
				cv2.circle(output_img, (x,y), 3, (0,255,0), -1)
				
			# Update Tracking Paths
			tracking_paths = new_tracking_paths
			
			# Draw Lines
			cv2.polylines(output_img, [np.int32(tp) for tp in tracking_paths], False, (0,150,0))
			
		# After Skipping Correct Number Of Frames
		if not frame_index % num_frames_jump:
			# Create Mask And Draw Circles
			mask = np.zeros_like(frame_gray)
			mask[:] = 255
			for x,y in [np.int32(tp[-1]) for tp in tracking_paths]:
				cv2.circle(mask, (x,y), 6, 0, -1)
				
			# Compute Good Features To Track
			feature_points = cv2.goodFeaturesToTrack(frame_gray, mask=mask, maxCorners=500, qualityLevel=0.3,
													 minDistance=7, blockSize=7)
			
			# If Feature Points Exist Append To Tracking Paths
			if feature_points is not None:
				for x,y in np.float32(feature_points).reshape(-1,2):
					tracking_paths.append([(x,y)])
					
		# Update Variables
		frame_index += 1
		prev_gray = frame_gray
		
		# Display Output
		cv2.imshow("Optical Flow", output_img)
		
		# Init Key Listener
		# If 'ESC': Exit
		k = cv2.waitKey(1)
		if k == 27:
			break
			
	
	
if __name__ == "__main__":
	# Start Tracker
	start_tracking()
	
	# Cleanup
	cap.release()
	cv2.destroyAllWindows()