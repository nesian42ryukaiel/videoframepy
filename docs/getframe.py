# -------------------------------------------------------------------- #
# extract frames from video
# -------------------------------------------------------------------- #

import cv2

vidcap = cv2.VideoCapture('./test/input/test.mp4')
fps = vidcap.get(cv2.CAP_PROP_FPS)                     # Do I need this?
totalNoFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)   # Or this?
durationInSeconds = float(totalNoFrames) / float(fps)  # Or this?

count = 0  # Do I really need the counting method in the main logic?

while(vidcap.isOpened()):
    ret, image = vidcap.read()
    # omit this resizing then, ...
    image = cv2.resize(image, (960, 540))

    if (int(vidcap.get(1)) % int(fps) == 0):
        # send the extracted image to the server one by one
        # LOGIC GOES HERE
        # following test code remains for mental stability until the end
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite('./test/output/frame%d.png' % count, image)
        count += 1
        if count >= durationInSeconds: vidcap.release()
