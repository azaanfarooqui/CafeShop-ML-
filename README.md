# CafeShop-ML-
 This project utilizes computer vision to enable user interaction through hand gestures, allowing intuitive menu selections. The system captures webcam input, detects hand movements, and records user choices, offering a unique and interactive experience.


The code involves using a webcam to detect hand gestures and make selections from a menu displayed on the screen. Let's break down the code step by step:

1. Libraries and Global Variables
The code starts by importing necessary libraries, including os, cv2 (OpenCV), and HandDetector from cvzone.
The global variable x2 is a list of options representing a menu.
2. man Function
The man function takes three parameters and assigns them to global variables a1, a2, and a3.
3. video_camera Function
The video_camera function captures video from the webcam, sets up a background image, and loads images for modes and icons.
It uses the HandDetector class to detect hand gestures.
The user can make selections by closing certain fingers. The selections are visualized using ellipses on the screen.
After each selection, an icon is added at the bottom of the screen.
The selections are stored in selectionList.
The program pauses briefly after each selection.
The function continuously displays the background image with selections and icons.
4. User Input and File Writing
The program prompts the user to input their name.
The video_camera function is then called.
After exiting the function, the selected options are printed based on the global variables a1, a2, and a3.
The user's name and selections are written to a text file named "orders.txt".
