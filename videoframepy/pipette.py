# -------------------------------------------------------------------- #
# pipette.py
#
# extracts average rgb color value of a given image
# -------------------------------------------------------------------- #

import cv2
import numpy as np


class Pipette:
    def __init__(self, im):
        self.im = cv2.imread(im)
        self.color = np.array(self.im).mean(axis=(0, 1))
        # print('initiated')

    def extract(self):
        # print(self.color)
        return self.color


if __name__ == '__main__':
    p = Pipette('../garbage/lena.png')
    r = Pipette('../garbage/red.png')
    print(p.extract())
    print(int(p.extract()[0]))
    print(int(p.extract()[1]))
    print(int(p.extract()[2]))
    print(r.extract())
    print(int(r.extract()[0]))
    print(int(r.extract()[1]))
    print(int(r.extract()[2]))
