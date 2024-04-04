import cv2
import numpy as np

# Define the color ranges for each face of the Rubik's Cube
color_ranges = {
    'red': [(0, 100, 100), (5, 255, 255)],
    'orange': [(5, 100, 100), (15, 255, 255)],
    'yellow': [(25, 100, 100), (35, 255, 255)],
    'green': [(45, 100, 100), (75, 255, 255)],
    'blue': [(100, 100, 100), (130, 255, 255)],
    'white': [(0, 0, 100), (180, 50, 255)]
}

def detect_colors(image):
    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Initialize an empty dictionary to store the color masks
    color_masks = {}

    # Iterate over each color range
    for color, (lower, upper) in color_ranges.items():
        # Create a mask for the current color range
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        
        # Apply a threshold to the mask to ignore the background
        _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        
        color_masks[color] = mask

    return color_masks

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Detect color masks in the frame
        color_masks = detect_colors(frame)

        # Display the original frame
        cv2.imshow('Rubik\'s Cube', frame)

        # Display each color mask in a separate window
        for color, mask in color_masks.items():
            cv2.imshow(f'Mask - {color}', mask)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()