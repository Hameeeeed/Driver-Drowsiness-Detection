#Driver Drowsiness Detection System

A real-time system designed to alert drivers when signs of drowsiness are detected, helping to reduce accidents caused by fatigue. This project uses Python, OpenCV, and Dlib for image processing and drowsiness detection.

Table of Contents

Overview
Features
Technologies
Installation

Usage
Project Structure

Limitations

Future Enhancements
Contributors
Overview
The Driver Drowsiness Detection System is designed to improve road safety by monitoring the driver’s eye movements and alerting them if signs of drowsiness are detected. The system captures input from a webcam, analyzes eye blinks, and triggers an alarm if drowsiness is detected for over 5 seconds.

Features
Real-Time Detection: Uses a webcam to monitor driver alertness.
Alarm System: Triggers an alarm when drowsiness is detected.
Threaded Alerts: Ensures continuous monitoring without lag.
User-Friendly: Simple interface that runs smoothly on most systems.

technologies
Python: Core programming language.
OpenCV: For video capture and image processing.
Dlib: For facial landmarks and eye detection.
Threading: Used to handle alerts and prevent system lag.
Installation

Clone this repository:
bash
Copy code
git clone https://github.com/Hameeeeed/driver-drowsiness-detection.git
Change to the project directory:

bash
Copy code
cd driver-drowsiness-detection
Install the required packages:
bash
Copy code
pip install -r requirements.txt

Usage
Ensure a webcam is connected and positioned to capture the driver’s face.
Run the main program:

bash
Copy code
python main.py

The system will begin monitoring and alerting as necessary.

Project Structure

bash
Copy code
driver-drowsiness-detection/

├── detection/              
 Detection and alert modules
├── main.py                
 Main script to run the detection system
├── requirements.txt       
Python dependencies
└── README.md              
Project documentation

Limitations
Lighting Conditions: Performance may degrade in low-light environments.
Camera Position: Requires a direct view of the driver’s face for effective monitoring.

Future Enhancements
Improved Accuracy: Explore advanced ML models to enhance detection.
Vehicle Integration: Connect with vehicle systems for automated braking.
Customization: Allow users to set alert sensitivity and alarm duration.
