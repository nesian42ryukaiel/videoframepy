# -------------------------------------------------------------------- #
# pipette.py
#
# extracts average rgb color value of a given image
# -------------------------------------------------------------------- #

import videoframepy.responder as vr
import cv2
import numpy as np


class Pipette(vr.Responder):
    def __init__(self, im):
        super(Pipette, self).__init__()
        self.im = im    # requires result of imdecode;
                        # OTOH the old code: self.im = cv2.imread(im)
        self.color = np.array(self.im).mean(axis=(0, 1))
        # print('initiated')

    def run(self):
        # print(self.color)
        return self.color
