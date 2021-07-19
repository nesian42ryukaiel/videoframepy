import unittest
from videoframepy import *

class BufferTest(unittest.TestCase):
    def test_initialization(self):
        b = buffer.Buffer()
        self.assertIsInstance(b, buffer.Buffer)
        
        bufferLength = b.length()
        self.assertEqual(bufferLength, 0)

    def test_push(self):
        b = buffer.Buffer()
        self.assertIsInstance(b, buffer.Buffer)
        
        fr1 = frame.Frame("frame1", [])
        fr2 = frame.Frame("frame2", [])
        fr3 = frame.Frame("frame3", [])
        self.assertIsInstance(fr1, frame.Frame)
        self.assertNotIsInstance(fr2, extractor.Extractor)
        self.assertNotIsInstance(fr3, buffer.Buffer)
        
        b.push(fr1)
        b.push(fr2)
        b.push(fr3)
        
        bufferLength = b.length()
        self.assertEqual(bufferLength, 3)
    
if __name__ == '__main__':
    unittest.main()