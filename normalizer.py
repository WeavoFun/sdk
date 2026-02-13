class Normalizer:
    def transform(self, raw_tx: dict) -> dict:
        return {
            "id": raw_tx["tx_id"],
            "notional": raw_tx["value"],
            "gas_fee": raw_tx["gas"],
            "actor": raw_tx["wallet"]
        }
