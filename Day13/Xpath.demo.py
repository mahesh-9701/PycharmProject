from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:/Drivers/chromedriver")
driver=webdriver.Chrome(service=ser_obj)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
# Absolute Xpath
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()
#Relative Xpath
# driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()
#or and and operator
# driver.find_element(By.XPATH,"//input[@class='search_query form-control ac_input' or type='text']").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[@type='submit' and @name='submit_search']").click()

#contains()   and starts-with()  functions
# driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()
# text() function :Text function is used to identify the inner text
driver.find_element(By.XPATH,"//a[text()='Women']").click()

