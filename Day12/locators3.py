from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:/Drivers/chromedriver")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://www.facebook.com/")
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("123")
# driver.find_element(By.XPATH,".inputtext").send_keys("123")
# driver.find_element(By.CSS_SELECTOR,"button._42ft").click()
# driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email address or phone number']").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid='royal_email']").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[aria-label=Password]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,".inputtext[aria-label=Password]").send_keys("abc@gmail.com")
