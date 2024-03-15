import requests

url = "http://127.0.0.1:8080/sc"

# Replace 'your_api_key' with your actual API key
headers = {'API': 'abcd', 'User': 'smart_cafe_two'}


# Replace 'path_to_your_image.jpg' with the actual path to your image file
files = {'image': open('1.jpeg', 'rb')}

response = requests.post(url, headers=headers, files=files)

if response.status_code == 201:
    # image_id = response.json()['image_id']
    print(response.json())
elif response.status_code == 400:
    print("Error: ", response.json()['error'])
elif response.status_code == 401:
    print("Error: ", response.json()['error'])
else:
    print("Error: ", response.text)
