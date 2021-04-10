from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, notification):
        pass

class Notification(ABC):
    def __init__(self, subject_id, subject_state):
        self.subject_id = subject_id
        self.subject_state = subject_state
