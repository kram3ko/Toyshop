import random
import sys
import threading
import requests
import logging
from django.apps import AppConfig

logger = logging.getLogger("pinger")


def start_ping():
    def ping():
        try:
            requests.get(
                "https://toys-shop.onrender.com/ping/",
                headers={
                    "User-Agent": "Toyshop service"
                }
            )
            logger.info("Ping sent")
        except Exception as e:
            logger.error(f"Ping error: {e}")
        threading.Timer(random.randrange(45, 90), ping).start()

    ping()


class PingerConfig(AppConfig):
    name = "pinger"

    def ready(self):
        if "gunicorn" in sys.argv[0] or "runserver" in sys.argv:
            print("🔥 START SERVER!", flush=True)
            start_ping()
