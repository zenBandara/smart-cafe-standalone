import requests

url = "http://127.0.0.1:5000/register_face"

# Replace 'your_api_key' with your actual API key
headers = {'API': 'abcd', 'User': 'slt', 'user_id': '992568653V'}

# Replace 'path_to_your_image.jpg' with the actual path to your image file
files = {'image': open('cup.jpg', 'rb')}
data = {'nic': '992565683V'}

response = requests.post(url, headers=headers, files=files, data=data)

if response.status_code == 201:
    # image_id = response.json()['image_id']
    print(response.json())
elif response.status_code == 400:
    print("Error: ", response.json()['error'])
elif response.status_code == 401:
    print("Error: ", response.json()['error'])
else:
    print("Error: ", response.text)
