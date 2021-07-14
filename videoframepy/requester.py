# -------------------------------------------------------------------- #
# requester.py
# sends extracted frames from target video to server
# -------------------------------------------------------------------- #

from flask import Flask, request, Response
import jsonpickle
import numpy as np


class Requester:
    def __init__(self, dst):
        self.destination = dst

    def send(self, buffer):
        for i in buffer:
            pass
            # send item to destination (server link in this case)

    def run(self):
        self.send()