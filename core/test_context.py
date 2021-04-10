import unittest
from context import Context, IoRegister


@IoRegister
class Pin :
    def __init__(self, id):        
        self.id = id
        self.l_obs = []

    def add_observer(self, o):
        self.l_obs.append(o)

    def set_state(self, state):
        self.state = state
        self.notify()

    def low(self):
        self.state = 0
        self.notify()

    def high(self):
        self.state = 1
        self.notify()

    def value(self):
        return self.state

    def notify(self):
        for ob in self.l_obs:
            ob.update(self.state)

class IhmElement:
    def __init__(self):
        self.state = 0
        pass

    def update(self, state):
        self.state = state

    def refresh(self):
        print("Ihm ELT " , self.state)
        return self.state


class TestContext(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInstanciate(self):
        ctx = Context()
        ctx.add_io_ihm_interface(Pin, IhmElement)
        p1 = Pin(1)
        p1.low()
        p1.high()
        assert(ctx.list_ihm_elts[0].state == 1)

if __name__ == "__main__":
    unittest.main() # run all tests