from singleton_pattern import Singleton
from observer_pattern import Subject, Notification



@Singleton
class Context:
    def __init__(self):
        self.list_ios = []  
        self.dic_interface = {}
        self.ihm = None

    def add_io_ihm_interface(self, io_class, ihmelt_class):
        self.dic_interface[io_class.__name__] = ihmelt_class

    def register_io(self, io):
        self.list_ios.append(io)
        ihm_elt_class = self.dic_interface[io.__class__.__name__]
        ihm_elt_obj = ihm_elt_class()
        io.register_observer(ihm_elt_obj)
        if self.ihm != None :
            self.ihm.add_element(io.id, ihm_elt_obj)

    def attach_ihm(self, ihm):
        self.ihm = ihm

class IoTemplate (Subject):
    def __init__(self):
        Subject.__init__(self)
        self.state= None
        self.observers = []        
        self.id="Not named IO"

    def register_observer(self, observer):
        self.observers.append(observer)        

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observer(self):
        for obs in self.observers:
            obs.update(Notification(self.id, self.state))

def IoRegister(cls):
    class Io(cls, IoTemplate):
        __doc__ = cls.__doc__
        
        def __init__(self, *args, **kwargs):     
            super(Io, self).__init__(*args, **kwargs)  
            IoTemplate.__init__(self) 
            Context().register_io(self)

    #TODO : may not work with different IO type ()
    Io.__name__ = cls.__name__
    return Io

def notify(func):
    def func_with_notification(*args, **kwargs):
        valeur = func(*args, **kwargs)
        args[0].notify_observer()
        return valeur
    return func_with_notification
        



