# Importing required libraries
import cv2
import numpy as np
import dlib
from imutils import face_utils
import threading
from playsound import playsound  # Importing playsound for alert sound

# Initialize the camera and face detectors
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Status markers for current state
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# To avoid playing sound continuously
alarm_on = False

# Function to compute the distance between two points
def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

# Function to detect if the eyes are blinking
def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # Checking if eyes are blinked
    if ratio > 0.25:
        return 2  # Eyes open
    elif 0.21 < ratio <= 0.25:
        return 1  # Eyes partially open
    else:
        return 0  # Eyes closed

# Function to play alarm sound in a separate thread
def play_alarm():
    while alarm_on:
        playsound('wake_up.mp3')

# Main loop for detection
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    face_frame = frame.copy()  # Initialize face_frame even if no face is detected
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blinked(landmarks[36], landmarks[37], 
            landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], 
            landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        # Determine eye blink status
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                if not alarm_on:  # Start alarm if not already on
                    alarm_on = True
                    alarm_thread = threading.Thread(target=play_alarm)
                    alarm_thread.start()

        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
                if not alarm_on:  # Start alarm if not already on
                    alarm_on = True
                    alarm_thread = threading.Thread(target=play_alarm)
                    alarm_thread.start()

        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "Active :)"
                color = (0, 255, 0)
                alarm_on = False  # Stop the alarm when eyes are fully open
                if 'alarm_thread' in locals():  # Ensure the thread is stopped
                    alarm_thread.join()

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    # Display the result frame
    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        alarm_on = False
        if 'alarm_thread' in locals():  # Ensure the thread is stopped
            alarm_thread.join()
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
    