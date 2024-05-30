import cv2

def read_first_frame(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        exit()

    # Read the first frame
    success, frame = cap.read()

    # Check if the frame was read successfully
    if not success:
        print("Error: Unable to read frame.")
        exit()

    # Release the video capture object
    cap.release()

    return frame