import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver_service = Service(executable_path="/Users/saeedjabbar/Downloads/chromedriver_mac_arm64/chromedriver")
# driver = webdriver.Chrome(service=driver_service)

driver = webdriver.Chrome()

driver.get("https://google.com")
time.sleep(2)

driver.quit()
