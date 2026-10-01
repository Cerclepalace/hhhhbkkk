from .models import Candidate

class DiscoveryEngine:
    def discover(self) -> list[Candidate]:
        return [
            Candidate("demo-001", "synthetic", "Demo Affiliate Offer", 25.0, True),
            Candidate("demo-002", "synthetic", "Secondary Offer", 10.0, True),
        ]
