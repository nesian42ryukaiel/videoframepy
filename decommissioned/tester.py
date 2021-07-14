# -------------------------------------------------------------------- #
# main test module
# -------------------------------------------------------------------- #

from videoframepy import *


class Tester:

    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run_all(self):
        for i in self.tests:
            i.run()


if __name__ == '__main__':
    t = Tester()
    t.add_test(temp)
    t.run_all()
    print('tester working...')
