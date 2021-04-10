def Singleton(cls):
    class Single(cls):
        __doc__ = cls.__doc__
        _initialized = False
        _instance = None
        
        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
            return cls._instance
                       
        def __init__(self, *args, **kwargs):
            if self._initialized:
                return
            super(Single, self).__init__(*args, **kwargs)
            self.__class__._initialized = True
    return Single

@Singleton
class Registry:
    def __init__(self):
        self.cpt = 0  
        self.entries = []  

    def up(self):
        self.cpt = self.cpt + 1
        return self.cpt

    def add(self, entry):
        self.entries.append(entry)

def IoRegister(cls):
    class IoRegistrant(cls):
        __doc__ = cls.__doc__

        def __init__(self, *args, **kwargs):
            Registry().add(self)
            super(IoRegistrant, self).__init__(*args, **kwargs)

    return IoRegistrant

@IoRegister
class Pin:
    def __init__(self, id):
        self.id = id
        self.state = 0

    def low(self):
        self.state = 0
    
    def high(self):
        self.state = 1


p1 = Pin(1)
p2 = Pin(2)
p3 = Pin(3)

for entry in Registry().entries:
    print(entry.id)
