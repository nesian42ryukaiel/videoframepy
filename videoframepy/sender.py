# -------------------------------------------------------------------- #
# sends extracted frames from target video to server
# -------------------------------------------------------------------- #

from flask import Flask, request, Response
import jsonpickle
import numpy as np


class Sender:
    def __init__(self, dest):
        self.dest = dest
        self.storage = []

    def send(self):
        pass

    def run(self):
        self.send()
