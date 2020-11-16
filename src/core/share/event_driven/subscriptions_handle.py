from abc import ABCMeta, abstractmethod
from src.core.share.event_driven.event_bus import EventBus
class SubscriptionHandle(metaclass=ABCMeta):
    """
    This Class has the abstract method to execute the Use Case
    """
    def __init__(self, event_type, event_bus:EventBus):
        """SubscriptionHandle Constructor"""
        self.event_bus = event_bus
        self.event_type = event_type
    @abstractmethod
    def execute(self) -> None : pass

    def __call__(self):
        self.event_bus.subscribe(self.event_type, self.execute)