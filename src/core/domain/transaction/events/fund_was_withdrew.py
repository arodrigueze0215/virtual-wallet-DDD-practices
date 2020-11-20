from src.core.share.domain.domain_event import DomainEvent
class FundWasWithDrew(DomainEvent):
    """
    Fund Was Deposited Event Domain
    """
    def __init__(self, transaction_id):
        super().__init__(transaction_id)