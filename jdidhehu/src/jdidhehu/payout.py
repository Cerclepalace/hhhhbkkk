from dataclasses import dataclass
from .commission import Commission, CommissionStatus

@dataclass(frozen=True)
class PayoutSnapshot:
    estimated: float
    approved: float
    payable: float
    paid: float

class PayoutStatusEngine:
    def snapshot(self, commissions: list[Commission]) -> PayoutSnapshot:
        return PayoutSnapshot(
            estimated=sum(c.estimated_amount for c in commissions),
            approved=sum(c.approved_amount for c in commissions if c.status in {
                CommissionStatus.APPROVED, CommissionStatus.PAYABLE, CommissionStatus.PAID
            }),
            payable=sum(c.approved_amount for c in commissions if c.status == CommissionStatus.PAYABLE),
            paid=sum(c.paid_amount for c in commissions if c.status == CommissionStatus.PAID),
        )
