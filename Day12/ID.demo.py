from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:/Drivers/chromedriver")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
# driver.find_element(By.ID,"small-searchterms").send_keys("laptop")
# #driver.find_element(By.NAME,"q").send_keys("laptop")
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
driver.quit()