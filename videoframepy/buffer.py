# -------------------------------------------------------------------- #
# buffer.py
# stores extracted frame images
# -------------------------------------------------------------------- #

import videoframepy.frame as c_frame


class Buffer:
    def __init__(self):
        self.buffer = []

    def push(self, frame):
        eligible = isinstance(frame, c_frame.Frame)
        if eligible:
            self.buffer.append(frame)

