import videoframepy.extractor
import videoframepy.buffer
import videoframepy.requester


class Test:
    def __init__(self, resource, fps, dst):
        self.x = videoframepy.extractor.Extractor(resource, fps)
        self.b = videoframepy.buffer.Buffer()
        self.r = videoframepy.requester.Requester(dst)

    def test(self):
        self.x.run(self.b)
        self.r.request(self.b)


if __name__ == '__main__':
    t = Test('test/input/test.mp4', 30, 'localhost:5000')
    t.test()
