from abc import abstractmethod, ABC
from observer_pattern import Observer, Notification

class Ihm(ABC):
    @abstractmethod
    def add_element(self, name, element):
        pass
    
    @abstractmethod
    def refresh_elements(self):
        pass

class IhmBasic(Ihm):
    def __init__(self):
        self.elements = {}
    
    def add_element(self, name, element):
        self.elements[name] = element

    def refresh_elements(self):
        count = 0
        for elt in self.elements:
            count += self.elements[elt].refresh()
        return count

class IhmElement(Observer):
    def __init__(self):
        pass

    @abstractmethod
    def refresh(self):
        pass

class IhmEltPin(IhmElement):
    def __init__(self):
        IhmElement.__init__(self)
        self.subject_id = 0
        self.subject_state = 0
        
    def update(self, notification):        
        self.subject_id = notification.subject_id
        self.subject_state = notification.subject_state
        self.refresh()

    def refresh(self):
        print ("pin", self.subject_id , " => ", self.subject_state)
        return self.subject_state
        
