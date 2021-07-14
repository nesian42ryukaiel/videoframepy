# -------------------------------------------------------------------- #
# first test: does the directory connect? YES!
# -------------------------------------------------------------------- #

# import videoframepy
import docs.ping


class Tester:
    def __init__(self):
        self.p = docs.ping.Ping()

    def test(self):
        self.p.run()


if __name__ == '__main__':
    t = Tester()
    t.test()
