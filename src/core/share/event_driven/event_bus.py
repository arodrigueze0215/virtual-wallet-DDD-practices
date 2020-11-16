from abc import ABCMeta, abstractmethod
class EventBus(metaclass=ABCMeta):
    """
    docstring
    """
    def __init__(self):
        self._subscriptors = {}

    def publish(self, events):
        #Publish all the subscribers
        for event in events:
            callback_list = self._subscriptors.get(event.get_type(), [])
            if len(callback_list) > 0:
                for callback in callback_list:
                    callback()      

    def subscribe(self, event_type, callback):
        subscribers = self._subscriptors.get(event_type, [])
        subscribers.append(callback)
        self._subscriptors[event_type] = subscribers