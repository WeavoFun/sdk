import random
import time

class MempoolStream:
    def __init__(self, network: str):
        self.network = network

    def listen(self):
        while True:
            time.sleep(1)
            yield {
                "tx_id": random.randint(1000, 9999),
                "value": random.uniform(1000, 100000),
                "gas": random.uniform(0.1, 2.0),
                "wallet": f"wallet_{random.randint(1,10)}"
            }
