import cv2
import numpy as np
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk, ImageGrab

# Callback function for mouse events
def get_hsv_range(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = frame[y,x]
        pixel_bgr = frame[y,x].reshape((1, 1, 3))
        hsv_image = cv2.cvtColor(pixel_bgr, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([max(hsv_image[0][0][0] - threshold, 0), 50, 50])
        upper_bound = np.array([min(hsv_image[0][0][0] + threshold, 179), 255, 255])

        # Set a label in the GUI to display the HSV range
        hsv_range_label.config(text=f"HSV Range: {lower_bound}, {upper_bound}")

# Function to start video capture and select color
def select_color():
    global frame
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', get_hsv_range)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Build the GUI
root = Tk()
root.title("Color Picker")

frame = None
threshold = 40

select_btn = Button(root, text="Select Color", command=select_color)
select_btn.pack()

hsv_range_label = Label(root, text="HSV Range:")
hsv_range_label.pack()

# Run the GUI
root.mainloop()
