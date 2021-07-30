import videoframepy.extractor
import videoframepy.buffer
import videoframepy.requester


class Test:
    def __init__(self, resource, fps, dst, dir):
        self.x = videoframepy.extractor.Extractor(resource, fps)
        self.b = videoframepy.buffer.Buffer()
        self.r = videoframepy.requester.Requester(dst, dir)

    def test(self):
        self.x.run(self.b)
        self.r.request(self.b)


if __name__ == '__main__':
    # t = Test('./garbage/input/test.mp4', 30, 'http://192.168.0.13:5000')
    # t = Test('./garbage/input/test.mp4', 30, 'http://127.0.0.1:5000', '/predict')
    t = Test('./garbage/input/test.mp4', 30, 'replace_with_server_ngrok_url', '/predict')
    t.test()
