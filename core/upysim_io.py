
from observer_pattern import Subject, Notification

class Io (Subject):
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


