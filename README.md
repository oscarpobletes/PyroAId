# Pyro AId

Pyro AId is a project aimed at detecting and analyzing fire-related events using YOLOv8, an advanced object detection model. It leverages computer vision to make predictions on video files, images, and live camera feeds.

## Project Structure

### Training

**YOLOv8_training.ipynb**:
- **Description**: This Jupyter notebook trains a YOLOv8 model using a dataset from Roboflow.
- **Features**:
  - Imports required libraries.
  - Initializes the dataset.
  - Trains the YOLOv8 model.
  - Visualizes training results.
  - Validates the trained model.

### Prediction

**YOLOv8_prediction.py**:
- **Description**: This Python script uses the trained YOLOv8 model to make predictions on video files, images, or live camera feeds.
- **Features**:
  - Initializes the YOLO model with trained weights.
  - Allows for predictions on different sources (camera, video, image).
  - Configurable prediction parameters (e.g., confidence threshold, image size).

## Requirements

- `ultralytics`: For YOLOv8 utilities and model operations.
- `roboflow`: For dataset management and downloading.

Install the necessary libraries using pip:

```bash
pip install ultralytics
pip install roboflow
```
## Getting Started

1. **Training**:
   - Replace `TOKEN_PLACEHOLDER` in `YOLOv8_training.ipynb` with your Roboflow API key.
   - Run the notebook to train the YOLOv8 model.

2. **Prediction**:
   - Ensure the trained weights (`best.pt`) are available.
   - Update the paths for video, image, or camera in `YOLOv8_prediction.py`.

## Running the Prediction Script

1. **Edit the `YOLOv8_prediction.py` file**:
   - Set the `video_path`, `image_path`, or `camera_path` to the desired input source.
   
2. **Execute the script**:
   ```bash
   python YOLOv8_prediction.py
   ````

Feel free to share and contribute!


