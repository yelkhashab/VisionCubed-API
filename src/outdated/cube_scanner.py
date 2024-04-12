import cv2
import numpy as np

# Define the color ranges for each face of the Rubik's Cube
color_ranges = {
    'R': [(170, 100, 100), (179, 255, 255)],
    'O': [(7, 100, 100), (15, 255, 255)],
    'Y': [(25, 100, 100), (35, 255, 255)],
    'G': [(45, 100, 100), (75, 255, 255)],
    'B': [(100, 100, 100), (130, 255, 255)],
    'W': [(100, 0, 100), (180, 50, 255)]
}

# Define the mapping of center colors to face names
color_to_face = {
    'R': 'F',
    'B': 'R',
    'O': 'B',
    'G': 'L',
    'W': 'U',
    'Y': 'D'
}

# Define the mapping of face names to center colors
face_to_color = {
    'F': 'R',
    'R': 'B',
    'B': 'O',
    'L': 'G',
    'U': 'W',
    'D': 'Y'
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

def get_cube_state(color_masks, frame):
    # Define the reference cube state
    cube_state = {
        'U': ['W'] * 9,
        'R': ['B'] * 9,
        'F': ['R'] * 9,
        'D': ['Y'] * 9,
        'L': ['G'] * 9,
        'B': ['O'] * 9
    }

    # Define the minimum number of pixels required to assign a color
    min_pixels = 50

    # Get the frame dimensions
    height, width, _ = frame.shape

    # Calculate the size and position of each cubie region
    cubie_size = min(height, width) // 6
    offset_x = (width - cubie_size * 3) // 2
    offset_y = (height - cubie_size * 3) // 2

    # Iterate over each face and color
    for color, face in color_to_face.items():
        colors = cube_state[face]
        for i in range(9):
            # Calculate the coordinates of the current cubie region
            row = i // 3
            col = i % 3
            x1 = offset_x + col * cubie_size
            y1 = offset_y + row * cubie_size
            x2 = x1 + cubie_size
            y2 = y1 + cubie_size

            # Draw the cubie region outline on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Count the number of pixels of each color within the cubie region
            color_counts = {}
            for c, mask in color_masks.items():
                color_counts[c] = np.count_nonzero(mask[y1:y2, x1:x2])

            # Find the color with the maximum count
            max_color = max(color_counts, key=color_counts.get)

            # Assign the color only if it meets the minimum pixel count
            if color_counts[max_color] >= min_pixels:
                colors[i] = max_color
            else:
                colors[i] = 'unknown'

            # Draw the cubie region outline with the face color
            if face == color_to_face[color]:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return cube_state

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Initialize an empty dictionary to store the cube state
    cube_state = {}

    # Define the face order for scanning
    face_order = ['F', 'R', 'B', 'L', 'U', 'D']

    # Iterate over each face
    for face in face_order:
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            # Detect color masks in the frame
            color_masks = detect_colors(frame)

            # Get the current cube state and draw cubie regions on the frame
            current_face_state = get_cube_state(color_masks, frame)

            # Add the current face state to the cube state dictionary
            cube_state[face] = current_face_state[face]

            # Display the original frame with cubie regions
            cv2.imshow('Rubik\'s Cube', frame)

            # Display the color mask for the current face
            mask = color_masks[face_to_color[face]]
            cv2.imshow(f'Mask - {face}', mask)

            # Wait for the user to press the space key
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):
                break

            # Break the loop if 'q' is pressed
            if key == ord('q'):
                break
            
        # Break the loop if 'q' is pressed
        if key == ord('q'):
            break
        
        # Close the mask window for the current face
        cv2.destroyWindow(f'Mask - {face}')

    # Print the final cube state
    print(cube_state)

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()