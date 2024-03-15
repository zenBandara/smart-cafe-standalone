import requests
import cv2

import plate_detector
API_KEY = "abcd"
USER = "smart_cafe_two"
url = "http://127.0.0.1:8080/sc"


def image_name():
    import uuid
    img_id = uuid.uuid4().int
    return str(img_id)


def plate_det(img_name):
    # return True
    # YOLOv8 dices detector
    if plate_detector.detect_plate(img_name):
        return True
    else:
        return False


while True:
    cap = cv2.VideoCapture('http://192.168.1.2:8080/video')  # put ip camera link
    ret, frame = cap.read()
    image_name = "realtime"
    image_save = "images/img/" + image_name + ".jpg"
    cv2.imwrite(image_save, frame)

    if plate_det(image_name):
        # Call API
        #  Header
        headers = {'API': API_KEY, 'User': USER}
        # BODY
        files = {'image': open("images/img/realtime.jpg", 'rb')}
        response = requests.post(url, headers=headers, files=files)

        # Working with response
        if response.status_code == 201:
            print(response.json())
        elif response.status_code == 400:
            print("Error: ", response.json()['error'])
        elif response.status_code == 401:
            print("Error: ", response.json()['error'])
        else:
            print("Error: ", response.text)



