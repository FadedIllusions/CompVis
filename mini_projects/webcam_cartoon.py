# Import Needed Packages
import numpy as np
import cv2


def print_howto():
	print("""
		Change Cartoonizing Mode Of Image:
			1. Cartoonize Without Color -- Press 's'.
			2. Cartoonize With Color -- Press 'c'.
			
		Press 'ESC' To Exit
	""")
	
	
def cartoonize_image(img, ksize=5, sketch_mode=False):
	# Init Need Vars For Function
	num_repetitions, sigma_color, sigma_space, ds_factor = 10, 5, 7, 4
	# Convert Image To Grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# Apply Median Blur To Grayscale Image
	img_gray = cv2.medianBlur(img_gray, 7)
	
	# Find Edges And Make Mask
	edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=ksize)
	ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
	
	# Resize Image For Quicker Processing
	img_small = cv2.resize(img, None, fx=1.0/ds_factor, fy=1.0/ds_factor, interpolation=cv2.INTER_AREA)
	
	if sketch_mode:
		# Convert Back To BGR, Erode Slightly, Blur
		img_sketch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
		kernel = np.ones((3,3), np.uint8)
		img_eroded = cv2. erode(img_sketch, kernel, iterations=1)
		return cv2.medianBlur(img_eroded, ksize=5)
	
	# Iterate Over Number Of Repetitions
	for i in range(num_repetitions):
		# Apply Bilater Filter
		img_small = cv2.bilateralFilter(img_small, ksize, sigma_color, sigma_space)
		# Return To Normal Size
		img_output = cv2.resize(img_small, None, fx = ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR)
		
		# Generate Layer Of Zeros (Black)
		dst = np.zeros(img_gray.shape)
		# Add To Image Via Mask
		dst = cv2.bitwise_and(img_output, img_output, mask=mask)
		
		# Return Image
		return dst
	
	
if __name__ == "__main__":
	print_howto()
	
	# Initialize Stream Object -- Onboard Webcam
	stream = cv2.VideoCapture(0)
	
	# If You Want To Start Recording Stream From Open
	#	
	# Define Codec
	# Init VideoWriter
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	#output = VideoWriter(outvid, fourcc, float(fps), size, is_color)
	#output = cv2.VideoWriter('output/cartoon.avi', fourcc, 20.0, (640,480))
	
	# Initiate Current Mode Variable
	cur_mode = None
	
	# While There Is A Video Stream
	while True:
		# Grab Frame
		ret, frame = stream.read()
		# Resize Frame As Desired (fx,fy)
		frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
		
		# Listen For Key Presses
		k = cv2.waitKey(1) & 0xFF
		
		# If 'ESC' Is Pressed: Exit
		if k == 27:
			break
		
		if k != -1 and k != 255 and k != cur_mode:
			cur_mode = k
			
		# If 's' Pressed, Init 'Sketch' Effect
		if cur_mode == ord('s'):
			frame = cartoonize_image(frame, ksize=5, sketch_mode=True)
			cv2.imshow('Cartoonize', frame)
		# If 'c' Is Pressed, Init 'Cartoon' Effect
		elif cur_mode == ord('c'):
			frame = cartoonize_image(frame, ksize=5, sketch_mode=False)
			cv2.imshow('Cartoonize', frame)
		# Otherwise, Show Normal Frame
		else:
			cv2.imshow('Cartoonize', frame)
		
		# If Saving To Video File
		# Write Frame To File
		output.write(frame)
			
			
	# Cleanup			
	stream.release()
	cv2.destroyAllWindows()