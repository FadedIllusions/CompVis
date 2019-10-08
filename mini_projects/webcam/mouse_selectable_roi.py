# 'ESC' To Exit

# Import Needed Packages
import numpy as np
import cv2


def update_pts(params, x, y):
	# Define Globally Accessible Variables
	# To Hold Initial (x,y) Coords Of Mouse Click
	# And (x,y) Coord Of Click Release
	global x_init, y_init
	params["pt_top_left"] = (min(x_init, x), min(y_init, y))
	params["pt_bottom_right"] = (max(x_init, x), max(y_init, y))
	
	# Invert Colors Within Repective Region Of Frame
	frame[y_init:y, x_init:x] = 255 - frame[y_init:y, x_init:x]
	
	
def draw_rectangle(event, x, y, flags, params):
	global x_init, y_init, drawing
	
	# First Click Inits The Initial Rectangle Point
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		x_init, y_init = x, y
		
	# While Button Pressed, Updata Diagonal Rectangle Point
	elif event == cv2.EVENT_MOUSEMOVE and drawing:
		update_pts(params, x, y)
		
	# Once Button Is Released
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		update_pts(params, x, y)
		
		
if __name__ == '__main__':
	# Init Drawing And Event Parameters
	drawing = False
	event_params = {"pt_top_left": (-1,-1), "pt_bottom_right":(-1,-1)}
	
	# Initialize Video Stream
	stream = cv2.VideoCapture(0)
	
	# If Wanting To Record From Start
	#
	# Define Codec
	# Init VideoWriter
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	#output = VideoWriter(outvid, fourcc, float(fps), size, is_color)
	#output = cv2.VideoWriter('selectable_roi.avi', fourcc, 20.0, (640,480))
	
	# If Camera Opened Correctly
	if not stream.isOpened():
		raise IOError("[INFO] Cannot Open Camera...")
	
	# Create Future Window For Stream
	cv2.namedWindow("Stream")
	
	# Bind draw_rectangle Function To Every Mouse Event
	cv2.setMouseCallback("Stream", draw_rectangle, event_params)
	
	while True:
		# Grab Frame
		ret, frame = stream.read()
		# Resize, If Needed/Desired, For Processing
		#frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
		# Grab Init And End (x,y) Coords
		(x0,y0), (x1,y1) = event_params["pt_top_left"], event_params["pt_bottom_right"]
		# Define Region Of Frame 
		frame[y0:y1, x0:x1] = 255 - frame[y0:y1, x0:x1]
		
		# Display Stream
		cv2.imshow("Stream", frame)
		
		# Write Frame To File
		#output.write(frame)
		
		# Listen For Key Press
		# If 'ESC': Exit
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
			
	
	# Cleanup
	stream.release()
	cv2.destroyAllWindows()