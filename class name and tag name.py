from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:/Drivers/chromedriver")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php")
sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container bx-clone")
print(len(sliders))
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
driver.close()