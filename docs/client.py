# -------------------------------------------------------------------- #
# client.py is imported from:
# https://gist.github.com/edumucelli/c2843ed1f6e13ed4706d63be87a0d671
# -------------------------------------------------------------------- #

import requests  # "a simple, yet elegant HTTP library"
import json      # supported by Python
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('webgi.jpg')

# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)

# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(response.text)

# expected output: {u'message': u'image received. size=124x124'}
