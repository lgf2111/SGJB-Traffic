from datetime import datetime
from pytz import timezone
from time import sleep
from os import getenv

# Local Imports
from logger import logging
from webapp import flask_run

from automation import driver
from automation.download import download_images


TZ = timezone(getenv("TZ"))
URL = getenv("URL")


if __name__ == "__main__":
    flask_run()
    while True:
        try:
            while True:
                now = datetime.now(tz=TZ)
                print(f"\r{now}", end="", flush=True)
                if now.minute in [0, 30]:
                    download_images(URL, TZ)
                sleep(1)
        except KeyboardInterrupt:
            driver.close()
        except Exception as e:
            logging.error(f"Error: {e}")
