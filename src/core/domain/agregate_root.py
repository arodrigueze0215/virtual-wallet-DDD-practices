from src.core.share.domain.domain_event import DomainEvent
from abc import ABCMeta
class AgregateRoot(metaclass=ABCMeta):
    """
    Let save and get all the DomainEvents.
    """
    _domainEventList = list()

    def __init__(self, agregate_root_id):
        self.agregate_root_id = agregate_root_id

    def register(self, domainEvent: DomainEvent):
        """ Save the domain evento on the list"""
        self._domainEventList.append(domainEvent)

    def get_all_domain_event(self) -> list:
        return self._domainEventList