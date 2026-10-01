from dataclasses import dataclass
from enum import Enum

class EventType(str, Enum):
    LINK_CREATED = "LINK_CREATED"
    CLICK = "CLICK"
    LEAD = "LEAD"
    CONVERSION = "CONVERSION"
    COMMISSION_PENDING = "COMMISSION_PENDING"

@dataclass(frozen=True)
class TrackingEvent:
    event_id: str
    event_type: EventType

class TrackingLedger:
    def __init__(self):
        self.events: list[TrackingEvent] = []

    def record(self, event: TrackingEvent) -> None:
        self.events.append(event)

    def count(self, event_type: EventType) -> int:
        return sum(e.event_type == event_type for e in self.events)
