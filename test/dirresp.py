# -------------------------------------------------------------------- #
# first test: does the directory connect? YES!
# -------------------------------------------------------------------- #

# import videoframepy
import videoframepy.ping


class Tester:
    def __init__(self):
        self.p = videoframepy.ping.Ping()

    def test(self):
        self.p.ping()

if __name__ == '__main__':
    t = Tester()
    t.test()
