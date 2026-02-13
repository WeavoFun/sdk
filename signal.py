from dataclasses import dataclass

@dataclass
class Signal:
    tx_id: int
    confidence: float
    label: str
