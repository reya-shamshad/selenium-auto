import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Loads Selenium Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Creates Browser Object
browser = webdriver.Chrome()

# Opens Google
browser.get('http://www.google.com/')

# Wait for 5 Second
time.sleep(5)

# Close Browser
driver.close()

