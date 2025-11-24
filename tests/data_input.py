import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")

options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/text-box")

full_name_field = driver.find_element("xpath","//input[@id='userName']")
full_name_field.clear()
full_name_field.send_keys("Oleg Olegov")

time.sleep(3)

email_field = driver.find_element("xpath","//input[@id='userEmail']")
email_field.clear()
email_field.send_keys("olegolegov_test@gmail.com")

time.sleep(3)

current_address_field = driver.find_element("xpath","//textarea[@id='currentAddress']")
current_address_field.clear()
current_address_field.send_keys("ul.Pushkina, d.8")

time.sleep(3)

permanent_address_field = driver.find_element("xpath","//textarea[@id='permanentAddress']")
permanent_address_field.clear()
permanent_address_field.send_keys("ul.Kolotushkina, d.12")

time.sleep(3)

full_name_attribute = full_name_field.get_attribute("value")
email_attribute = email_field.get_attribute("value")
current_address_attribute = current_address_field.get_attribute("value")
permanent_address_attribute = permanent_address_field.get_attribute("value")

assert "Oleg Olegov" in full_name_attribute, "Ошибка: данные некорректные"
assert "olegolegov_test@gmail.com" in email_attribute, "Ошибка: данные некорректные"
assert "ul.Pushkina, d.8" in current_address_attribute, "Ошибка: данные некорректные"
assert "ul.Kolotushkina, d.12" in permanent_address_attribute, "Ошибка: данные некорректные"

driver.quit()