# Fabric Defect Detection

This project implements a fabric defect detection system using Streamlit for a user-friendly interface and YOLOv8 for object detection. 

### Project Overview

Manual fabric defect inspection is time-consuming and prone to human error. This project addresses this challenge by offering an automated solution for fabric quality control. 

### Features

* Upload fabric images for defect detection.
* Visualize the detected defects with labels.

### Prerequisites

* Python 3.6 or later
* Streamlit
* YOLOv8 ([https://github.com/topics/yolov8](https://github.com/topics/yolov8))

### Installation

1. Clone this repository.
2. Create a new virtual environment (recommended).
3. Install required dependencies:
   ```bash
   pip install streamlit yolov8
   ```
4. Download pre-trained YOLOv8 weights (compatible with your dataset) and place them in the project directory. 

### Usage

1. Run the application:
   ```bash
   streamlit run main.py
   ```
2. Access the application in your web browser at http://localhost:8501.
3. Upload a fabric image and the model will predict and visualize any detected defects.


