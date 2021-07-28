# -------------------------------------------------------------------- #
# responder.py
#
# interface for the server side's duty
# -------------------------------------------------------------------- #

from abc import ABC, abstractmethod


class Responder(ABC):
    def __init__(self):
        super(Responder, self).__init__()

    @abstractmethod
    def run(self):
        pass
