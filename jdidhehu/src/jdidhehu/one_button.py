from dataclasses import dataclass, field
from .discovery import DiscoveryEngine

@dataclass
class OneButtonResult:
    discovered: int
    qualified: int
    offers: int
    actions_required: list[str] = field(default_factory=list)

class OneButtonEngine:
    def __init__(self):
        self.discovery = DiscoveryEngine()

    def start(self, target_eur: float = 100.0) -> OneButtonResult:
        if target_eur <= 0:
            raise ValueError("target_eur must be positive")
        candidates = self.discovery.discover()
        qualified = [c for c in candidates if c.qualified]
        return OneButtonResult(
            discovered=len(candidates),
            qualified=len(qualified),
            offers=len(qualified),
            actions_required=["Provider approval and real conversion are still required."],
        )
