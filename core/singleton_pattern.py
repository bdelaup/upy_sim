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
