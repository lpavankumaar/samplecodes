from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://pythonexamples.org")
print(driver.title)
driver.find_element_by_link_text("Basics").click()
driver.close()