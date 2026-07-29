import os
import cv2

# Find the number corresponding to the USB CAM
s = 2

source = cv2.VideoCapture(s)
source.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
source.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

actual_width = source.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = source.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Resolution: {actual_width} x {actual_height}")
print(f"Press Esc to close the window and capture the image.")

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

filename = "capture.png"
dst_folder = "img"
ret, frame = source.read()
if ret:
    cv2.imwrite(os.path.join(dst_folder, filename), frame)
    print(f"Saved \"{filename}\" to folder \"{dst_folder}\".")

source.release()
cv2.destroyWindow(win_name)
