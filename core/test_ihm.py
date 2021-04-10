import unittest
from ihm import Ihm, IhmEltBasic
from upysim_io import Io

class TestSubject(Io):
    def __init__(self):
        Io.__init__(self)
        self._state = 0

    def action(self):
        self._state = self._state+1
        self.notify_observer()


class TestIhm(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBasic(self):
        subj = TestSubject()
        ihm_elt = IhmEltBasic()
        subj.register_observer(ihm_elt)

        ihm_elt.refresh()
        assert(ihm_elt.refresh() == 0)
        subj.action()
        assert(ihm_elt.refresh() == 1)
        

    def testIhm(self):
        subj1 = TestSubject()
        subj2 = TestSubject()
        subj3 = TestSubject()

        ihm_elt1 = IhmEltBasic()
        ihm_elt2 = IhmEltBasic()
        ihm_elt3 = IhmEltBasic()
        ihm_elt4 = IhmEltBasic()
        ihm_elt5 = IhmEltBasic()
        
        subj1.register_observer(ihm_elt1)
        subj1.register_observer(ihm_elt2)
        subj1.register_observer(ihm_elt3)
        subj2.register_observer(ihm_elt4)
        subj3.register_observer(ihm_elt5)

        ihm = Ihm()

        ihm.add('1', ihm_elt1)
        ihm.add('2', ihm_elt1)
        ihm.add('3', ihm_elt1)
        ihm.add('4', ihm_elt1)
        ihm.add('5', ihm_elt1)

        assert (ihm.refresh() == 0)

        for i in range(5):
            subj1.action()
            subj2.action()
            subj3.action()
            i=i

        assert (ihm.refresh() == 25)
        assert (ihm_elt1.refresh() == 5)


if __name__ == "__main__":
    unittest.main() # run all tests
    