# Lucas-Kanage Differential Method -- Really Good For Tracking Corners In Images

# Import Needed Packages
import numpy as np
import cv2


# Init Video Stream
cap = cv2.VideoCapture(0)

# Set Parameters For ShiTomasi Corner Detection
feature_params = dict(maxCorners = 100,
					  qualityLevel = 0.3,
					  minDistance = 7,
					  blockSize = 7)

# Set Parameters For Lucas Kanade Optical Flow
lucas_kanade_params = dict(winSize = (15,15),
						  maxLevel =2,
						  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create Random Colors
color = np.random.randint(0, 255, (100,3))

# Take First Frame And Find Corners
_, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Find Initial Corner Locations
prev_corners = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)

# Create Mask Image For Drawing Purposes
mask = np.zeros_like(prev_frame)


while True:
	_, frame = cap.read()
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Calculate Optical Flow
	new_corners, status, errors = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prev_corners, None, **lucas_kanade_params)
	
	# Select And Store Good Points
	good_new = new_corners[status==1]
	good_old = prev_corners[status==1]
	
	# Draw Tracks
	for i,(new,old) in enumerate(zip(good_new,good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		mask = cv2.line(mask, (a,b), (c,d), color[i].tolist(), 2)
		frame = cv2.circle(frame, (a,b), 5, color[i].tolist(), -1)
		
	img = cv2.add(frame, mask)
	
	# Show Optical Flow
	cv2.imshow("Optical Flow -- Lucas-Kanade", img)
	
	# Define Key Listener
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
		
	# Update Previous Frame And Point
	prev_gray = frame_gray.copy()
	prev_corners = good_new.reshape(-1,1,2)
	
	
# Cleanup
cap.release()
cv2.destroyAllWindows()