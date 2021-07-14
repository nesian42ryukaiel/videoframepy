# -------------------------------------------------------------------- #
# main test module
# -------------------------------------------------------------------- #

from videoframepy import *


class Tester:

    def __init__(self):
        self.tests = []

    def addtest(self, test):
        self.tests.append(test)

    def runall(self):
        for i in self.tests:
            i.run()


if __name__ == '__main__':
    t = Tester()
    t.addtest(temp)
    t.runall()
    print('tester working...')
