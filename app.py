from fastapi import FastAPI
from fastapi.responses import FileResponse
import cv2

app = FastAPI()

def capture_photo():
    # Open the video device (the webcam)
    cap = cv2.VideoCapture(0)  # 0 is usually the device index for the default webcam

    if not cap.isOpened():
        print("Error: Could not open video device.")
        return None

    # Set video frame width and height (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Save the frame as an image file
        photo_path = 'webcam_photo.jpg'
        cv2.imwrite(photo_path, frame)
        cap.release()
        return photo_path
    else:
        cap.release()
        print("Error: Could not capture frame.")
        return None

@app.get("/photo")
def get_photo():
    photo_path = capture_photo()
    if photo_path:
        return FileResponse(photo_path, media_type='image/jpeg', filename='webcam_photo.jpg')
    else:
        return {"error": "Could not capture photo"}
