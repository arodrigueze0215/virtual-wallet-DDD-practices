from src.core.share.domain.domain_event import DomainEvent
class AccountWasCreated(DomainEvent):
    """Account was created Domain event"""

    def __init__(self, account_id):
        super().__init__(account_id)
