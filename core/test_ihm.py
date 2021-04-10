import unittest
from ihm import IhmBasic, IhmEltPin
from observer_pattern import Subject, Notification


class SubjectTest(Subject):
    def __init__(self):        
        self.state = 0
        self.observers = []

    def register_observer(self, obs):
        self.observers.append(obs)

    def notify_observer(self):
        for ob in self.observers:
            ob.update(Notification("none", self.state))

    def action(self):
        self.state = self.state+1
        self.notify_observer()

    def remove_observer(self, ob):
        pass
    


class TestIhm(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBasic(self):
        subj = SubjectTest()
        ihm_elt = IhmEltPin()
        subj.register_observer(ihm_elt)

        ihm_elt.refresh()
        assert(ihm_elt.refresh() == 0)
        subj.action()
        assert(ihm_elt.refresh() == 1)
        

    def testIhm(self):
        subj1 = SubjectTest()
        subj2 = SubjectTest()
        subj3 = SubjectTest()

        ihm_elt1 = IhmEltPin()
        ihm_elt2 = IhmEltPin()
        ihm_elt3 = IhmEltPin()
        ihm_elt4 = IhmEltPin()
        ihm_elt5 = IhmEltPin()
        
        subj1.register_observer(ihm_elt1)
        subj1.register_observer(ihm_elt2)
        subj1.register_observer(ihm_elt3)
        subj2.register_observer(ihm_elt4)
        subj3.register_observer(ihm_elt5)

        ihm = IhmBasic()

        ihm.add_element('1', ihm_elt1)
        ihm.add_element('2', ihm_elt1)
        ihm.add_element('3', ihm_elt1)
        ihm.add_element('4', ihm_elt1)
        ihm.add_element('5', ihm_elt1)

        self.assertEqual(ihm.refresh_elements(), 0)

        for i in range(5):
            subj1.action()
            subj2.action()
            subj3.action()
            i=i

        self.assertEqual (ihm.refresh_elements() , 25)
        self.assertEqual (ihm_elt1.refresh() , 5)


if __name__ == "__main__":
    unittest.main() # run all tests
    