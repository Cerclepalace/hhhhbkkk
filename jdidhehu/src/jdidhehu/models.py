from dataclasses import dataclass

@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    platform: str
    product: str
    commission_eur: float
    qualified: bool = True
