# -------------------------------------------------------------------- #
# server.py is imported from:
# https://gist.github.com/edumucelli/c2843ed1f6e13ed4706d63be87a0d671
# -------------------------------------------------------------------- #

from flask import Flask, request, Response
import jsonpickle   # "a library for the two-way conversion of
import numpy as np  #  complex Python objects and JSON        "
import cv2
import datetime
from videoframepy import pipette


# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/garbage/output/', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # either recognize object or calculate average color scheme here
    pip = pipette.Pipette(img)
    bgr = pip.run()
    blu = int(bgr[0])
    grn = int(bgr[1])
    red = int(bgr[2])

    cv2.imwrite('./garbage/output/result_{}.jpg'.format(datetime.datetime.now().timestamp()), img)

    # cv2.imshow('temp_test_mat', img)  # will not work in pycharm
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}; avg. color={:x}{:x}{:x}'.format(img.shape[1], img.shape[0], red, grn, blu)
                }  # add average color scheme or recognized object here
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
# app.run(host="0.0.0.0", port=5000)
app.run()
