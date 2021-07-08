# -------------------------------------------------------------------- #
# main logic of part 1
# assumed to be starting at home directory
# activate venv by:
#     % source ~/venv/firstvenv/bin/activate
# link at:
#     % python3 ~/repo/videoframepy/main.py
# -------------------------------------------------------------------- #

import cv2

vidcap = cv2.VideoCapture('./video/test.mp4')
fps = vidcap.get(cv2.CAP_PROP_FPS)
totalNoFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
durationInSeconds = float(totalNoFrames) / float(fps)

count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()
    image = cv2.resize(image, (960, 540))

    if (int(vidcap.get(1)) % int(fps) == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite('./stash/frame%d.png' % count, image)
        count += 1
        if count >= durationInSeconds: vidcap.release()
