import time
import requests
from lxml import etree
from selenium import webdriver


temp_link = "https://xingye.me/game/colortest/index.html"
while 1:
        try:
            driver = webdriver.Chrome()
            break
        except Exception:
            time.sleep(1)
driver.get(temp_link)
driver.find_elements_by_xpath('//*[@class="btn play-btn"]')[0].click()
i = 0
while(i < 60000):
    # boxs = driver.find_element_by_id('box')
    boxs = driver.find_elements_by_xpath('//*[@id="box"]/span')
    current = boxs[0] if boxs[0].value_of_css_property('background-color') == boxs[1].value_of_css_property('background-color') else boxs[2]
    for box in boxs:
        if current.value_of_css_property('background-color') == box.value_of_css_property('background-color'):
            current = box
        else:
            box.click()
            break


