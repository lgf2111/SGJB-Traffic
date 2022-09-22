# Main Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Interraction Imports
from selenium.webdriver.common.by import By

from os import getenv

# Replit
if getenv("REPL_OWNER"):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

else:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
