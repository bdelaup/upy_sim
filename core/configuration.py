from context import Context
from ihm import IhmEltPin
from machine import Pin

class ConfigureForR2:
    @classmethod
    def run(self):
        ctx = Context()
        ctx.add_io_ihm_interface(Pin, IhmEltPin)

