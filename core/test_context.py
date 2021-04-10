import unittest
from context import Context, IoRegister, notify
from ihm import IhmBasic


@IoRegister
class Pin :
    def __init__(self, id):        
        self.id = id
        self.l_obs = []


    @notify
    def set_state(self, state):
        self.state = state

    @notify
    def low(self):
        self.state = 0
    
    @notify
    def high(self):
        self.state = 1

    @notify
    def value(self):
        return self.state


class IhmElement:
    def __init__(self):
        self.state = 0
        pass

    def update(self, notification):
        self.state = notification.subject_state

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
        ctx.attach_ihm(IhmBasic())
        p1 = Pin(1)
        p1.low()
        p1.high()
        self.assertEqual(ctx.ihm.elements[p1.id].state , 1)

if __name__ == "__main__":
    unittest.main() # run all tests