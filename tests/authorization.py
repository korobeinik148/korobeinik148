import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

login_field = ("xpath", "//input[@type='email']")
password_field = ("xpath", "//input[@type='password']")
submit_button = ("xpath", "//button[@type='submit']")

driver.get("https://hyperskill.org/login")
time.sleep(5)
driver.find_element(*login_field).send_keys("alekseik@ya.ru")
driver.find_element(*password_field).send_keys("Qwerty132!")
driver.find_element(*submit_button).click()
time.sleep(5)


