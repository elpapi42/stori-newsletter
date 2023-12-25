import json
import logging
from datetime import datetime, timezone


logging.basicConfig(format=None, level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("httpcore").setLevel(logging.ERROR)


class Logger():
    @staticmethod
    def info(message: str, **properties) -> None:
        payload = {
            "message": message,
            "level": "INFO",
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            **properties
        }

        logging.info(json.dumps(payload))

    @staticmethod
    def error(message: str, **properties) -> None:
        payload = {
            "message": message,
            "level": "ERROR",
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            **properties
        }

        logging.error(json.dumps(payload))
