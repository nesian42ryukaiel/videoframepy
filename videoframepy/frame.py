# -------------------------------------------------------------------- #
# frame.py
# struct which stores id and image path
# -------------------------------------------------------------------- #

class Frame:
    def __init__(self, id, path):
        self.id = id
        self.path = path

    def demo(self):
        print(self.id, self.path)
