from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver.exe")

driver.get("https://lms.umt.edu.pk/my/")

driver.find_element_by_id("identifierId").send_keys("F2019105035@umt.edu.pk")

time.sleep(5)

driver.find_element_by_css_selector("#identifierNext > div > button").click()

time.sleep(5)

driver.find_element_by_name("password").send_keys(u5Fy@27X)

time.sleep(5)

driver.find_element_by_css_selector("#passwordNext > div > button").click()