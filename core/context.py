from singleton_pattern import Singleton


@Singleton
class Context:
    def __init__(self):
        self.list_ios = []  
        self.list_ihm_elts = []
        self.dic_interface = {}

    def attach_ihm(self, ihm):
        self.list_ihm_elts.append(ihm)

    def add_io_ihm_interface(self, io, ihmelt_class):
        self.dic_interface[io.__name__] = ihmelt_class

    def attach_io(self, io):
        self.list_ios.append(io)
        ihm_elt_class = self.dic_interface[io.__class__.__name__]
        ihm_elt_obj = ihm_elt_class()
        io.register_observer(ihm_elt_obj)
        self.attach_ihm(ihm_elt_obj)
        
def IoRegister(cls):
    class IoRegistrant(cls):
        __doc__ = cls.__doc__
        
        def __init__(self, *args, **kwargs):
            # self.cls_name = cls.__name__            
            super(IoRegistrant, self).__init__(*args, **kwargs)        
            Context().attach_io(self)
    
    #TODO : may not work with different IO type ()
    IoRegistrant.__name__ = cls.__name__
    return IoRegistrant
        

