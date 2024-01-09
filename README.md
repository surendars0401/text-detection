#text-detection
#Text Detection and OCR with OpenCV and Tesseract
Introduction
This Python script uses the OpenCV library for computer vision and the Tesseract OCR engine to perform real-time text detection and optical character recognition (OCR) from a live video feed. The script captures frames from a webcam, processes them to detect text regions, and then performs OCR to recognize the text.

Prerequisites
Python 3.x
OpenCV
Tesseract OCR
pytesseract library
Webcam (for live video feed)

Make sure to install the required libraries using the following commands:

bash

pip install opencv-python
pip install pytesseract
Additionally, you need to install Tesseract OCR and set the path in the script (pytesseract.pytesseract.tesseract_cmd).

How to Run

Clone or download the repository.
Install the required libraries as mentioned above.
Adjust the path to the Tesseract OCR executable (tesseract_cmd) based on your installation.
Run the script.

Functionality

The script captures video frames from the default webcam (cv2.VideoCapture(0)).
It converts each frame to grayscale and applies bilateral filtering for noise reduction.
Adaptive thresholding is used to create a binary image to enhance text features.
Contours are then detected using OpenCV's findContours function to identify potential text regions.
Text regions are filtered based on width and height criteria, and OCR is applied to these regions.
OCR is performed at regular intervals (ocr_interval) to balance performance and accuracy.
A majority voting system is implemented to improve OCR accuracy over time.
The final recognized number is printed after reaching the specified number of frames (max_list_length).

Configuration

frame_display_delay: Delay in milliseconds for displaying each video frame.
text_detection_interval: Run text detection every n frames.
ocr_interval: Perform OCR every m frames that meet the text detection constraint.
max_list_length: Maximum length of the list for majority voting.

User Interaction

Press 'q' to exit the application.
Notes

Ensure that your webcam is connected and accessible.
Tesseract OCR must be properly installed and configured.
