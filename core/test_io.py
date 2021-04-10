import unittest
from context import IoTemplate
from observer_pattern import Observer



class Pin(IoTemplate) :
    def __init__(self):
        IoTemplate.__init__(self)

    def set_state(self, state):
        self.state = state
        self.notify_observer()

    def low(self):
        self.state = 0
        self.notify_observer()

    def high(self):
        self.state = 1
        self.notify_observer()

    def value(self):
        return self.state

class IhmElement(Observer):
    def __init__(self):
        self.state = 0
        pass

    def update(self, notification):
        self.state = notification.subject_state

    def refresh(self):
        print("Ihm ELT " , self.state)
        return self.state


class TestObserver(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPinChangedOut(self):
        pin = Pin()
        Ihm = IhmElement()
        pin.register_observer(Ihm)        
        pin.high()
        assert(Ihm.refresh() == 1)
        pin.low()
        assert(Ihm.refresh() == 0)


if __name__ == "__main__":
    unittest.main() # run all tests