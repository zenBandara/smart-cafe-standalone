import os.path
import shutil

from ultralytics import YOLO

model = YOLO('models/plate.pt')  # YOLOv8 model


def clean_fold():
    folder = 'images/plate'
    if os.path.exists(folder):
        for sub_folder in os.listdir(folder):
            full_path = os.path.join(folder, sub_folder)
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)


def detect_plate(image):
    # Clean the plate folder
    clean_fold()
    image_path = "images/img/" + image + ".jpg"  # img path
    result = model(source=image_path, save=True, max_det=1, conf=0.4, project="images/plate")
    data = result[0]
    print(len(data.boxes))
    # check result
    if len(data.boxes) > 0:
        return True  # plate is detected
    else:
        return False  # Plate not detected
