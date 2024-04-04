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

def get_cube_state(color_masks):
    # Define the reference cube state
    cube_state = {
        'up': ['white'] * 9,
        'right': ['red'] * 9,
        'front': ['green'] * 9,
        'down': ['yellow'] * 9,
        'left': ['orange'] * 9,
        'back': ['blue'] * 9
    }

    # Iterate over each face and color
    for face, colors in cube_state.items():
        for i in range(9):
            # Calculate the coordinates of the current cubie
            row = i // 3
            col = i % 3
            x = col * 50 + 25
            y = row * 50 + 25

            # Check the color of the current cubie
            for color, mask in color_masks.items():
                if mask[y, x] == 255:
                    colors[i] = color
                    break

    return cube_state

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Detect color masks in the frame
        color_masks = detect_colors(frame)

        # Get the current cube state
        cube_state = get_cube_state(color_masks)

        # Print the cube state
        for face, colors in cube_state.items():
            print(f"{face}: {colors}")

        # Display the original frame
        cv2.imshow('Rubik\'s Cube', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()