from selenium import webdriver
import urllib.request
browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.get('https://www.ais.tku.edu.tw/EleCos/login.aspx')
elem = browser.find_element_by_id('bn_new_confirm')
# elem.get_attribute("Value")  # Make Sure this is the refresh button
elem.click()  # Refresh!

img = browser.find_element_by_css_selector("img[id^='imgCONFM']")
url = img.get_attribute('src')
urllib.request.urlretrieve(url, "confirm.png")
