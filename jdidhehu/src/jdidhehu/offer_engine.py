from dataclasses import dataclass
from math import ceil
from .models import Candidate

@dataclass(frozen=True)
class OfferAnalysis:
    target_eur: float
    commission_eur: float
    minimum_sales: int
    upfront_cost_eur: float
    payable_now: bool = False
    unknowns: tuple[str, ...] = ()

class OfferEngine:
    def analyse(self, offer: Candidate, target_eur: float) -> OfferAnalysis:
        if target_eur <= 0:
            raise ValueError("target_eur must be positive")
        if offer.commission_eur <= 0:
            raise ValueError("commission_eur must be positive")
        return OfferAnalysis(
            target_eur=target_eur,
            commission_eur=offer.commission_eur,
            minimum_sales=ceil(target_eur / offer.commission_eur),
            upfront_cost_eur=0.0,
            unknowns=("conversion_not_guaranteed", "provider_approval_required"),
        )
