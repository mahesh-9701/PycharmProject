from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:\Drivers\chromedriver")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
