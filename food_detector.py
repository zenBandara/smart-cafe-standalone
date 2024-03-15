from ultralytics import YOLO
import food_counter




def process(img_name):
    model_name = 'Models/best.pt'
    model = YOLO(model_name)
    image_path = "image/" + img_name + ".jpg"
    result = model(image_path, save_crop=True, conf=0.7, project="detect/" + img_name)

    food_count = food_counter.count_foods(img_name)
    return food_count

# print(process("cup.jpg"))
