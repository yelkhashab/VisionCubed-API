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

    # Create a mask to exclude the white color
    lower_white = np.array([0, 0, 100])
    upper_white = np.array([180, 50, 255])
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    hsv[white_mask > 0] = [0, 0, 0]

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

    # Define the mapping of center colors to face names
    color_to_face = {
        'green': 'front',
        'red': 'right',
        'blue': 'back',
        'orange': 'left',
        'white': 'up',
        'yellow': 'down'
    }

    # Iterate over each face and color
    for color, face in color_to_face.items():
        colors = cube_state[face]
        for i in range(9):
            # Calculate the coordinates of the current cubie
            row = i // 3
            col = i % 3
            x = col * 50 + 25
            y = row * 50 + 25

            # Check the color of the current cubie
            if color_masks[color][y, x] == 255:
                colors[i] = color

    return cube_state

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Initialize an empty dictionary to store the cube state
    cube_state = {}

    # Define the face order for scanning
    face_order = ['green', 'red', 'blue', 'orange', 'white', 'yellow']

    # Iterate over each face
    for color in face_order:
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            # Detect color masks in the frame
            color_masks = detect_colors(frame)

            # Display the original frame
            cv2.imshow('Rubik\'s Cube', frame)

            # Display the color mask for the current face
            mask = color_masks[color]
            cv2.imshow(f'Mask - {color}', mask)

            # Wait for the user to press the space key
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):
                # Get the current cube state
                cube_state = get_cube_state(color_masks)
                break

            # Break the loop if 'q' is pressed
            if key == ord('q'):
                break

        # Close the mask window for the current face
        cv2.destroyWindow(f'Mask - {color}')

    # Print the final cube state
    for face, colors in cube_state.items():
        print(f"{face}: {colors}")

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()