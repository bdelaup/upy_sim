import unittest
from observer_pattern import Observer, Subject, Notification


class ConcretSubject(Subject) :
    def __init__(self):
        self._state = 0
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)
        

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observer(self):
        for obs in self._observers:
            notification = Notification("E", self._state)
            obs.update(notification)

    def set_state(self, state):
        self._state = state
        self.notify_observer()


class ConcretObserver(Observer):
    def __init__(self):
        self.state = None

    def update(self, notification):
        self.state = notification.subject_state

class TestObserver(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNominal(self):
        subj = ConcretSubject()
        obs = ConcretObserver()
        subj.register_observer(obs)        
        subj.set_state(4)
        assert(obs.state == 4)
        subj.set_state(5)
        assert(obs.state == 5)

if __name__ == "__main__":
    unittest.main() # run all tests