# Capture And Display Video (From Onboard Webcam)
# Press 'q' To Exit

# Import Needed Packages
import cv2


# Init Video Capture -- Device 0, Onboard Webcam
stream = cv2.VideoCapture(0)

# Can Check If Capture Is Open
# while stream.isOpen():

while True:
	# Capture Frame
	ret, frame = stream.read()
	# ret = stream.set(3, 1280)
	# ret = stream.set(4, 960)
	
	# Convert To Grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Display Frame
	cv2.imshow("Video Stream", gray)
	
	# If 'q', Exit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		

# Cleanup
# Release Capture And Destroy Window
stream.release()
cv2.destroyAllWindows()


# You Can Obtain Frame Size Via stream.get(3) And stream.get(4)
# And, As Seen In Above Comments, Can Set Frame Size
# Larger Frame Sizes Are More Computationally Expensive

# See Following For More:
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get