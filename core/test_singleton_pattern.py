import unittest
from singleton_pattern import Singleton

@Singleton
class MyClass:
    def __init__(self):
        self.cpt = 0

    def inc(self):
        self.cpt = self.cpt+1

class TestObserver(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNominal(self):
        MyClass()
        assert(MyClass().cpt == 0)
        MyClass().inc()
        assert(MyClass().cpt == 1)


if __name__ == "__main__":
    unittest.main() # run all tests