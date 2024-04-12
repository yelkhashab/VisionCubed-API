import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for OpenCV
cv2.createTrackbar('hMin', 'image', 0, 179, nothing)
cv2.createTrackbar('sMin', 'image', 0, 255, nothing)
cv2.createTrackbar('vMin', 'image', 0, 255, nothing)
cv2.createTrackbar('hMax', 'image', 0, 179, nothing)
cv2.createTrackbar('sMax', 'image', 0, 255, nothing)
cv2.createTrackbar('vMax', 'image', 0, 255, nothing)

# Set initial value for MAX HSV trackbars.
cv2.setTrackbarPos('hMax', 'image', 179)
cv2.setTrackbarPos('sMax', 'image', 255)
cv2.setTrackbarPos('vMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions
    hMin = cv2.getTrackbarPos('hMin', 'image')
    sMin = cv2.getTrackbarPos('sMin', 'image')
    vMin = cv2.getTrackbarPos('vMin', 'image')
    hMax = cv2.getTrackbarPos('hMax', 'image')
    sMax = cv2.getTrackbarPos('sMax', 'image')
    vMax = cv2.getTrackbarPos('vMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Create HSV Image and threshold into a range.
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display output image
    cv2.imshow('image', output)

    # Wait longer to prevent freeze for videos.
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
