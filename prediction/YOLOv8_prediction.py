from ultralytics import YOLO

# Initialize the YOLO model with the path of the trained weights
modelo = YOLO('best.pt')

# Specify the video path
video_path = 'fire.mp4'

# Specify the image path
image_path = 'fire.jpg'

# Specify the camera path
camera_path = 0

# Make predictions on video file, image or live camera
modelo.predict(source = camera_path, imgsz=640, conf=0.6, save=True, show=True)
