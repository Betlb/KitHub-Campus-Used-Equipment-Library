# src/borrow/observer.py
# Generic implementation of the Observer design pattern.

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject, event, data=None):
        """Receive update from subject."""
        pass

class Subject:
    """
    The Subject owns some important state and notifies observers when the state changes.
    """
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach an observer."""
        self._observers.remove(observer)

    def notify(self, event, data=None) -> None:
        """Notify all observers about an event."""
        print(f"SUBJECT: Notifying observers about event: '{event}'...")
        for observer in self._observers:
            observer.update(self, event, data)