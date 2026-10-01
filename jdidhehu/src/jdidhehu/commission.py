from dataclasses import dataclass
from enum import Enum

class CommissionStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    PAYABLE = "PAYABLE"
    PAID = "PAID"
    REJECTED = "REJECTED"

@dataclass
class Commission:
    commission_id: str
    offer_id: str
    estimated_amount: float
    status: CommissionStatus = CommissionStatus.PENDING
    approved_amount: float = 0.0
    paid_amount: float = 0.0

    def transition(self, new_status: CommissionStatus, amount: float | None = None):
        allowed = {
            CommissionStatus.PENDING: {CommissionStatus.APPROVED, CommissionStatus.REJECTED},
            CommissionStatus.APPROVED: {CommissionStatus.PAYABLE, CommissionStatus.REJECTED},
            CommissionStatus.PAYABLE: {CommissionStatus.PAID},
            CommissionStatus.PAID: set(),
            CommissionStatus.REJECTED: set(),
        }
        if new_status not in allowed[self.status]:
            raise ValueError(f"Invalid transition: {self.status} -> {new_status}")
        if new_status == CommissionStatus.APPROVED:
            if amount is None or amount < 0:
                raise ValueError("approved amount required")
            self.approved_amount = amount
        if new_status == CommissionStatus.PAID:
            if amount is None or amount < 0:
                raise ValueError("paid amount required")
            self.paid_amount = amount
        self.status = new_status
