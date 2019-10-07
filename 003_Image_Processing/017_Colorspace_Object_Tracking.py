# Object Tracking Using Colorspaces
# In This Project, We're Going To Hone In On An Object, Within A Webcam Stream,
# Using The HSV Colorspace, So That We Can Track It Throughout The Video Stream

# When Looking Up Color Values Within The Range Of Your Desired Object,
# Keep In Mind That OpenCV's Hue (H) Value Is Scaled To An Input Range Of 180

# In My Case, I Am Tracking A Purple Object

# 'q' To Quit

# Import Needed Packages
import numpy as np
import cv2


# Print Command Options To CLI
print("[INFO] Press 'q' To Quit...")

# Init Video Stream
webcam = cv2.VideoCapture(0)


# Define Color Range Of Desired Object To Track
lower = np.array([120, 80, 65], dtype=np.uint8)
upper = np.array([145, 255, 255], dtype=np.uint8)




while True:
	# Grab Frame
	_, frame = webcam.read()
	
	# Convert Frame To HSV Colorspace
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# Mask ROI (Desired Object)
	mask = cv2.inRange(hsv, lower, upper)
	
	# Find Contours Within Mask
	# (Largest Continuous Lines)
	# So As To, Essentially, Get An Outline Of Object
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	
	# If There Are Contours Found
	if len(cnts)>0:
		# Delineate Purple Section/Area
		area = max(cnts, key=cv2.contourArea)
		# Get Dimensions Of Bounding Rectangle
		(x,y,w,h) = cv2.boundingRect(area)
		# Draw Rectangle Onto Frame, Around Tracked Area
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
	
	# Display Frame From Stream
	cv2.imshow("Original Stream", frame)
	#cv2.imshow("HSV Stream", hsv)
	#cv2.imshow("Mask", mask)
	
	# Capture Keypress
	# If 'q', Exit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		print("[INFO] Pressed 'q': Quiting...")
		break

# Cleanup
webcam.release()
cv2.destroyAllWindows()