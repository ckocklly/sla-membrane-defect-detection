import cv2
import sys

# Find the number corresponding to the USB CAM
s = 2

source = cv2.VideoCapture(s)
source.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
source.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)
