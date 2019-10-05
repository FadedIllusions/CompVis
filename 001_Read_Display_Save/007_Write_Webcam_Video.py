# Save Video From Webcam
# Press 'q' To Quit

# Import Needed Packages
import cv2


# Init Video Capture
stream = cv2.VideoCapture(0)

# Define Codec
# Init VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#output = VideoWriter(outvid, fourcc, float(fps), size, is_color)
output = cv2.VideoWriter('../videos/output.avi', fourcc, 20.0, (640,480))


# While Webcam Open
while(stream.isOpened()):
	# Grab Frame
	ret, frame = stream.read()
	
	# If Frame Received
	if ret == True:
		# Mirror Frame, Grayscale
		# Horizontal Flip: 0
		# Vertical Flip: 1
		# Both: -1
		frame = cv2.flip(frame, 1)
		
		# Write Mirrored Frame To File
		output.write(frame)
		
		# Display Frame
		cv2.imshow("Video Stream", frame)
		
		# Capture Keypress
		# If 'q', Exit
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
			
	else:
		break
		
# Cleanup
stream.release()
output.release()
cv2.destroyAllWindows()