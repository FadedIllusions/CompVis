# Accessing Image Properties

# Import Needed Packages
import cv2


# Load Image
image = cv2.imread("../images/flowers.png")

# Grab Image Shape
# Rows, Columns, Channels
dimensions = image.shape
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]

# Print To CLI
print("\nDimensions: ", dimensions)
print("Height: {}, Width: {}, Channels: {}\n".format(height,width,channels))

# Grab And Print Total Number Of Pixels
print("Pixels:", image.size)

# Grab Image Datatype
print("\nDatatype:", image.dtype)