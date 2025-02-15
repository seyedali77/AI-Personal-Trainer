# AI-Personal-Trainer
Pose Detection and Exercise Counter
Features
Real-Time Pose Detection: Processes video frames to detect human pose landmarks.

Exercise Counter: Calculates the angle of the right arm to accurately count repetitions.

Visual Feedback: Displays a progress bar, percentage indicator, repetition counter, and FPS on the video.

Custom Pose Module: Integrates a dedicated module (PoseModule) for pose detection and angle calculation.

Prerequisites
Python 3.x

OpenCV: For image and video processing.

NumPy: For numerical computations.

PoseModule: A custom module required for pose detection.

You can install the necessary Python packages using pip:
pip install opencv-python numpy


Setup and Usage
Video File: Place a video file named 6.mp4 in the project directory or update the file path in the code if needed.

PoseModule: Ensure that the PoseModule.py file is located in the same directory as your main script.

Run the Script: Execute the main script by running the following command in your terminal:
python main.py


The application will open a window displaying the video with pose detection outputs including the exercise counter and other visual aids.
How It Works
Frame Capture: The script opens the video using OpenCV and resizes each frame.

Pose Estimation: Through the poseDetector class in PoseModule, the code locates body landmarks.

Angle Calculation: It computes the angle between key landmarks (points 11, 13, and 15, corresponding to parts of the arm) to evaluate the movement.

Repetition Counting: The calculated angle is interpolated to generate a percentage that indicates progress in a single exercise repetition. When this percentage hits 100% or drops to 0%, the counter increments to record a complete curl.

Visual Display: Rectangles and text overlays show the progress bar, repetition count, and FPS directly on the video frame.


Troubleshooting
Indentation Issues: If you encounter an IndentationError, double-check the formatting of the code, especially the alignment of loops and conditional blocks.

Module Import Errors: Verify that PoseModule.py is correctly placed in the project directory and is free of errors.

Video File Problems: Ensure that the video file (6.mp4) exists and is accessible by the script.

Contributions
Contributions are welcome. If you have suggestions or improvements, feel free to fork the repository, open an issue, or submit a pull request.
