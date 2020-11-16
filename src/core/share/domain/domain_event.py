from abc import ABCMeta
import uuid
from datetime import datetime
class DomainEvent(metaclass=ABCMeta):
    """
    Domain event definition
    """
    _event_id: str
    _occurred_on: str

    def __init__(self, agregate_root_id):
        self._event_id = str(uuid.uuid4())
        self._occurred_on = datetime.now()
    
    def get_type(self):
        return self.__class__.__name__ 


