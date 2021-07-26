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
    t = Test('./temp_test_mat/input/temp_test_mat.mp4', 30, 'http://192.168.0.13:5000')
    t.test()
