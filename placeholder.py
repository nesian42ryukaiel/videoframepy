# -------------------------------------------------------------------- #
# placeholder
# -------------------------------------------------------------------- #

import cv2

vidcap = cv2.VideoCapture('./video/test.mp4')

count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()
    image = cv2.resize(image, (960, 540))

    if (int(vidcap.get(1)) % 30 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite('./stash/frame%d.png' % count, image)
        count += 1
        vidcap.release()
