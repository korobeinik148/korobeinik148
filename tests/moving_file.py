import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[3]")

time.sleep(2)

action.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()

time.sleep(2)