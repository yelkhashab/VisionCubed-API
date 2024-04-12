import cv2
import numpy as np
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk, ImageGrab

# Callback function for mouse events
def getHsvRange(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = frame[y,x]
        pixelBgr = frame[y,x].reshape((1, 1, 3))
        hsvImage = cv2.cvtColor(pixelBgr, cv2.COLOR_BGR2HSV)
        lowerBound = np.array([max(hsvImage[0][0][0] - threshold, 0), 50, 50])
        upperBound = np.array([min(hsvImage[0][0][0] + threshold, 179), 255, 255])

        # Set a label in the GUI to display the HSV range
        hsvRangeLabel.config(text=f"HSV Range: {lowerBound}, {upperBound}")

# Function to start video capture and select color
def selectColor():
    global frame
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', getHsvRange)

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

selectBtn = Button(root, text="Select Color", command=selectColor)
selectBtn.pack()

hsvRangeLabel = Label(root, text="HSV Range:")
hsvRangeLabel.pack()

# Run the GUI
root.mainloop()
