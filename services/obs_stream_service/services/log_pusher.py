import logging
import threading
from datetime import datetime

import requests

# Configure a thread-safe logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def push(text: str):
    def send_log():
        url = "http://127.0.0.1:8000/log"
        payload = {"line": text}
        try:
            requests.post(url, json=payload, timeout=2)
            logging.info(f"[log_pusher] Pushed log: {text}")
        except requests.RequestException as e:
            logging.error(f"[log_pusher] ERROR: Could not connect to log service: {e}")

    thread = threading.Thread(target=send_log, daemon=True)
    thread.start()


if __name__ == "__main__":
    log_text = f"{datetime.now().isoformat()} Hello, world!"
    if log_text:
        push(log_text)
    else:
        logging.info("Please provide a log message to push.")
