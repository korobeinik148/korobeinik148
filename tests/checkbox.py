import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

grid_button = ('xpath', '//a[@id="demo-tab-grid"]')
one = ('xpath', '//li[text()="One"]')
two = ('xpath', '//li[text()="Two"]')
three = ('xpath', '//li[text()="Three"]')

driver.get("https://demoqa.com/selectable")

driver.find_element(*grid_button).click()

time.sleep(2)

driver.find_element(*one).click()
driver.find_element(*two).click()
driver.find_element(*three).click()

time.sleep(2)

assert "active" in driver.find_element(*one).get_attribute("class"), "Элемент не кликнут"
assert "active" in driver.find_element(*two).get_attribute("class"), "Элемент не кликнут"
assert "active" in driver.find_element(*three).get_attribute("class"), "Элемент не кликнут"

driver.find_element(*one).click()
driver.find_element(*two).click()
driver.find_element(*three).click()

time.sleep(2)

assert "active" not in driver.find_element(*one).get_attribute("class"), "Элемент не кликнут"
assert "active" not in driver.find_element(*two).get_attribute("class"), "Элемент не кликнут"
assert "active" not in driver.find_element(*three).get_attribute("class"), "Элемент не кликнут"