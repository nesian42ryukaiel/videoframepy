# -------------------------------------------------------------------- #
# requester.py
# sends extracted frames from target video to server
# -------------------------------------------------------------------- #

from flask import Flask, request, Response
import jsonpickle
import videoframepy.frame as c_frame
import videoframepy.buffer as c_buffer


class Requester:
    def __init__(self, dst):
        self.destination = dst

    def request(self, buffer):
        eligible = isinstance(buffer, c_buffer.Buffer)
        if eligible:
            for i in buffer.buffer:
                datacheck = isinstance(i, c_frame.Frame)
                if datacheck:
                    item = i.path
                    # send item to destination (server link in this case)
                else:
                    print('frame invaild')
        else:
            print('buffer invalid')

    def run(self, buffer):
        self.request(buffer)
