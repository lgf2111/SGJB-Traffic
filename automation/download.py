import os
from datetime import datetime
import urllib.request as request
from threading import Thread

from logger import logging
from automation import driver, By


def create_folder(tz):
    folder = os.path.join(
        os.getcwd(),
        "collections",
        *datetime.now(tz=tz).strftime(r"%Y/%m/%d/%H%M").split("/"),
    )
    try:
        os.makedirs(folder)
    except OSError as e:
        logging.error(f"Error: {e}")
    return folder


def download_images(url, tz):
    folder = create_folder(tz)
    driver.get(url)
    images = driver.find_elements(By.CSS_SELECTOR, "img")
    for i, image in enumerate(images):
        src = image.get_attribute("src")
        opener = request.build_opener()
        opener.addheaders = [
            ("user-agent", "Mozilla/5.0"),
            eval(os.getenv("HEAD")),
        ]
        request.install_opener(opener)
        request.urlretrieve(src, os.path.join(folder, f"{i}.png"))


def download_images_thread(url, tz):
    t = Thread(target=download_images, args=(url, tz))
    t.start()
