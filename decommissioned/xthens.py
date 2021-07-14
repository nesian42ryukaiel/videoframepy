from videoframepy import extractor as xtr
from videoframepy import requester as snd


def xthens():
    address = 'http://localhost:5000'
    test_url = address + '/api/test'
    x = xtr.Extractor('test.jpg', 30)
    s = snd.Requester(test_url)
