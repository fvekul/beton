import requests
import os

# initialize the Keras API endpoint URL along with the input
# image path
KERAS_API_URL = "http://localhost:5000/beton"
IMAGE_PATH = "./test/Positive/00004.jpg" # change to your image

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
r = requests.post(KERAS_API_URL, files=payload).json()

# ensure the request was successful and print the result
if r["success"]:
    print("Tear detected: " + str(r["scheur"]))
else:
    print("Request failed")
