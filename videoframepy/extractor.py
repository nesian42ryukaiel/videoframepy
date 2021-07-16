# -------------------------------------------------------------------- #
# extractor.py
# extracts frames from target video
# -------------------------------------------------------------------- #

import cv2
import videoframepy.frame as c_frame
import videoframepy.buffer as c_buffer


class Extractor:

    def __init__(self, resource, fps):
        self.vid_cap = cv2.VideoCapture(resource)
        self.fps = fps

    def extract(self, buffer):  # storage is in Buffer
        eligible = isinstance(buffer, c_buffer.Buffer)
        if not self.vid_cap.isOpened():
            return
        while eligible:
            ret, image = self.vid_cap.read()
            if ret is False:
                print('a1', self.vid_cap.get(1))
                break
            if int(self.vid_cap.get(1)) % int(self.fps) == 0:
                fr = c_frame.Frame(self.vid_cap.get(1), image)
                buffer.push(fr)

    def run(self, storage):
        self.extract(storage)

# -------------------------------------------------------------------- #
#
# https://stackoverflow.com/questions/10475198/retrieving-the-current-frame-number-in-opencv
#
# You can also use cvGetCaptureProperty method
# (if you use old C interface).
#
# cvGetCaptureProperty(CvCapture* capture,int property_id);
# property_id options are below with definitions:
#
# CV_CAP_PROP_POS_MSEC 0
# CV_CAP_PROP_POS_FRAME 1
# CV_CAP_PROP_POS_AVI_RATIO 2
# CV_CAP_PROP_FRAME_WIDTH 3
# CV_CAP_PROP_FRAME_HEIGHT 4
# CV_CAP_PROP_FPS 5
# CV_CAP_PROP_FOURCC 6
# CV_CAP_PROP_FRAME_COUNT 7
#
# POS_MSEC is the current position in a video file,
# measured in milliseconds.
#
# POS_FRAME is the position of current frame in video
# (like 55th frame of video).
#
# POS_AVI_RATIO is the current position given
# as a number between 0 and 1
# (this is actually quite useful when you want to position a trackbar
#  to allow folks to navigate around your video).
#
# FRAME_WIDTH and FRAME_HEIGHT are the dimensions of
# the individual frames of the video to be read
# (or to be captured at the camera’s current settings).
#
# FPS is specific to video files and indicates
# the number of frames per second at which the video was captured.
# You will need to know this if you want to play back your video
# and have it come out at the right speed.
#
# FOURCC is the four-character code for the compression codec
# to be used for the video you are currently reading.
#
# FRAME_COUNT should be the total number of frames in video,
# but this figure is not entirely reliable.
#
# (from Learning OpenCV book )
#
# -------------------------------------------------------------------- #
