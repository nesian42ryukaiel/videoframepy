# -------------------------------------------------------------------- #
# requester.py
# sends extracted frames from target video to server
# -------------------------------------------------------------------- #

# from flask import Flask, request, Response
# import jsonpickle
import cv2
import requests
import videoframepy.frame as c_frame
import videoframepy.buffer as c_buffer


class Requester:
    def __init__(self, dst, dir):
        self.destination = dst
        self.directory = dir

    def request(self, buffer):
        eligible = isinstance(buffer, c_buffer.Buffer)
        if eligible:
            addr = self.destination
            drct = self.directory
            test_url = addr + drct
            content_type = 'image/jpeg'
            headers = {'content-type': content_type}
            for i in buffer.buffer:
                datacheck = isinstance(i, c_frame.Frame)
                if datacheck:
                    item = i.image
                    # send item to destination (server link in this case)
                    _, item_encoded = cv2.imencode('.jpg',item)
                    response = requests.post(test_url, data=item_encoded.tostring(), headers=headers)
                    print(response.text)
                else:
                    print('frame invaild')
        else:
            print('buffer invalid')

    def run(self, buffer):
        self.request(buffer)
