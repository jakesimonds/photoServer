import cv2

# Open the video device (the webcam)
cap = cv2.VideoCapture(0)  # 0 is usually the device index for the default webcam

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

# Set video frame width and height (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capture a single frame
ret, frame = cap.read()

if ret:
    # Save the frame as an image file
    cv2.imwrite('webcam_photo.jpg', frame)
    print("Photo saved as webcam_photo.jpg")
else:
    print("Error: Could not capture frame.")

# Release the video device
cap.release()
print('made it to end')