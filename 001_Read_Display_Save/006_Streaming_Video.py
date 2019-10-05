# Streaming Video From A File
# Press 'q' To Exit

# Import Needed Packages
import cv2


# Init Video Stream (From File)
stream = cv2.VideoCapture('video_filename.mp4')

# So Long As File Opens
while(stream.isOpened()):
	# Grab Frame From Video
	ret, frame = stream.read()
	
	# Convert To Grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Display Frame
	cv2.imshow("Video Stream", gray)
	
	# Capture Keypress
	# If 'q', Exit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
		
# Cleanup		
stream.release()
cv2.destroyAllWindows()