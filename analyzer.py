from core.signal import Signal
import random

class Analyzer:
    def evaluate(self, tx: dict) -> Signal:
        confidence = min(1.0, tx["notional"] / 100000 + random.random() * 0.2)
        return Signal(
            tx_id=tx["id"],
            confidence=confidence,
            label="whale_activity" if confidence > 0.7 else "normal"
        )
