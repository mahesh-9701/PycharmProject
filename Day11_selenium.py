from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:/Drivers/geckodriver")
driver=webdriver.Firefox(service=ser_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_name("email").send_keys("kotlaumamaheswarareddy@gmail.com")
driver.find_element_by_name("pass").send_keys("Facebook@02071997")
driver.find_element_by_name("login").click()