# -------------------------------------------------------------------- #
# extracts frames from target video
# -------------------------------------------------------------------- #

import cv2
import videoframepy.sender


class Extractor:

    def __init__(self, resource, framecount):
        self.vidcap = cv2.VideoCapture(resource)
        self.framecount = framecount

    def extract(self, storage):
        while self.vidcap.isOpened():
            ret, image = self.vidcap.read()
            if int(self.vidcap.get(1)) % int(self.framecount) == 0:
                storage.append(image)

    def run(self, storage):
        self.extract(storage)
