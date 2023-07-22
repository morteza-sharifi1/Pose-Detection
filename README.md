# Pose-Detection

# Pose Detection with Python

This repository contains a Python script for real-time pose detection, using the OpenCV, numpy, and MediaPipe libraries.

## Description 

The script `main.py` takes a video file as input and displays two windows: one with the original video where the pose landmarks and connections are overlaid, and another one where the landmarks and connections are drawn on a blank canvas.

## Requirements

- Python 3.7 or higher
- OpenCV
- numpy
- MediaPipe

## Installation

To run the script, you need to install the required Python packages. You can do this by running the following command:

pip install opencv-python numpy mediapipe

## Usage

To run the script, navigate to the directory containing `main.py` and the video file and run the following command:

python main.py

The script currently processes the video named '4.mp4', but you can change the filename in the script to process a different video.

While running, the script displays two windows:

1. 'PoseDetection': This window shows the original video with the detected pose landmarks and connections overlaid on the video.
2. 'extractedPose': This window shows the detected pose landmarks and connections drawn on a blank canvas.

To quit the program, press 'q'.

### demo
![demo](https://raw.githubusercontent.com/morteza-sharifi1/Pose-Detection/2.png)
