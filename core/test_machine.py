import unittest
from machine import Pin


class TestPin(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHighLow(self):
        p = Pin(1)
        p.high()
        assert(p.value() == 1)
        p.low()
        assert(p.value() == 0)
    

    def testValue(self):
        p = Pin(1)
        p.value(1)
        assert(p.value() == 1)
        p.value(5)
        assert(p.value() == 1)
        p.value(0)
        assert(p.value() == 0)
    

if __name__ == "__main__":
    unittest.main() # run all tests