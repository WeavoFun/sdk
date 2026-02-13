from core.mempool import MempoolStream
from core.normalizer import Normalizer
from core.analyzer import Analyzer
from utils.logger import log
import config

def run():
    stream = MempoolStream(network=config.NETWORK)
    normalizer = Normalizer()
    analyzer = Analyzer()

    for tx in stream.listen():
        structured = normalizer.transform(tx)
        signal = analyzer.evaluate(structured)

        if signal.confidence > config.SIGNAL_THRESHOLD:
            log(f"HIGH SIGNAL DETECTED: {signal}")

if __name__ == "__main__":
    run()
