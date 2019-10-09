# CAMShift (Continuously Adaptive Mean) Algorithm
# See Following Link For Further Reading:
# https://docs.opencv.org/3.3.1/db/df8/tutorial_py_meanshift.html

# Import Needed Packages
import numpy as np
import cv2

# Define Class To Handle Object Tracking Related Functions
class ObjectTracker(object):
	
	def __init__(self, scaling_factor=1.0):
		# Init Video Capture Object
		self.cap = cv2.VideoCapture(0)
		
		# Grab Frame From Video Capture
		_, self.frame = self.cap.read()
		
		# Scaling Factor For Captured Frame
		self.scaling_factor = scaling_factor
		
		# Resize Frame
		self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor,
								interpolation=cv2.INTER_AREA)
		
		# Create Window Within Which To Display Frame
		cv2.namedWindow("Object Tracker")
		
		# Set Mouse Callback To Track Mouse
		cv2.setMouseCallback("Object Tracker", self.mouse_event)
		
		# Init Rectangular Selection Variable
		self.selection = None
		
		# Init Tracking State Variable
		self.tracking_state = 0
		
		
	# Define Method To Track Mouse Events
	def mouse_event(self, event, x, y, flags, param):
		# Convert (x,y) Coords Into 16b Numpy Ints
		x, y = np.int16([x,y])
		
		# Check For Mouse Button Down Event
		if event == cv2.EVENT_LBUTTONDOWN:
			self.drag_start = (x, y)
			self.tracking_state = 0
			
		# Check If User Starts Selecting Region
		if self.drag_start:
			if flags & cv2.EVENT_FLAG_LBUTTON:
				# Extract Dimensions Of Frame
				h, w = self.frame.shape[:2]
				
				# Get Initial Position
				xi, yi = self.drag_start
				
				# Get Min And Max Values
				x0, y0 = np.maximum(0, np.minimum([xi, yi], [x, y]))
				x1, y1 = np.minimum([w, h], np.maximum([xi, yi], [x, y]))
				
				# Reset Selection Variable
				self.selection = None
				
				# Finalize Selection
				if x1-x0>0 and y1-y0>0:
					self.selection = (x0, y0, x1, y1)
					
			else:
				# If Selection Done, Start Tracking
				self.drag_start = None
				if self.selection is not None:
					self.tracking_state = 1
					
					
	# Method To Start Tracking Object
	def start_tracking(self):
		# Iterate Until User Presses 'ESC' Key
		while True:
			# Capture Frame From Webcame
			_, self.frame = self.cap.read()
				
			# Resize Input Frame
			self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor,
										interpolation=cv2.INTER_AREA)
				
			# Copy Frame
			copy = self.frame.copy()
				
			# Convert Frame To HSV
			hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
				
			# Create Masked Based On Predefined Thresholds
			mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
				
			# If Region Has Been Selected
			if self.selection:
				# Extract Coordinated Of Selected Rectangle
				x0, y0, x1, y1 = self.selection
					
				# Extract Tracking Window
				self.track_window = (x0, y0, x1-x0, y1-y0)
					
				# Extract ROI
				hsv_roi = hsv[y0:y1, x0:x1]
				mask_roi = mask[y0:y1, x0:x1]
					
				# Compute Histogram of ROI in HSV Using Mask
				hist = cv2.calcHist([hsv_roi], [0], mask_roi, [16], [0,180])
					
				# Normalize And Reshape Histogram
				cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX);
				self.hist = hist.reshape(-1)
					
				# Extract ROI From Frame
				copy_roi = copy[y0:y1, x0:x1]
				
				# Compute Image Negative (For Display Only)
				cv2.bitwise_not(copy_roi, copy_roi)
				copy[mask==0] = 0
					
			# If In "Tracking" Mode
			if self.tracking_state == 1:
				# Reset Selection Variable
				self.selection = None
					
				# Compute Histogram Back Projection
				hsv_backproj = cv2.calcBackProject([hsv], [0], self.hist, [0,180], 1)
					
				# Compute Bitwise AND Between Histogram Backprojection And Mask
				hsv_backproj &= mask
					
				# Define Termination Criteria For Tracker
				term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
					
				# Apply CAMShift On hsv_backproj
				track_box, self.track_window = cv2.CamShift(hsv_backproj, self.track_window, term_crit)
					
				# Draw Ellipse Around Object
				cv2.ellipse(copy, track_box, (0,255,0), 2)
					
			# Display Video Stream
			cv2.imshow("Object Tracker", copy)
				
			# Define Key Listener
			# If 'ESC': Exit
			k = cv2.waitKey(1) & 0xFF
			if k == 27:
				break
					
					
		# Cleanup
		cap.release()
		cv2.destroyAllWindows()
			
			
if __name__ == "__main__":
	# Start Tracker
	ObjectTracker().start_tracking()