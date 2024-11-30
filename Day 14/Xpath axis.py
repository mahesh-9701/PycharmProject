from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj=Service("C:/Drivers/chromedriver")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/self::a").text
# print(text_msg)
#parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/parent::td").text
# print(text_msg)
# driver.close()
#Child
# childs=text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/ancestor::tr/child::td")
# print(len(childs))
# driver.close()
#ancestor
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/ancestor::tr").text
# print(text_msg)
# driver.close()
#Descendent
# descendents=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/ancestor::tr/descendant::*")
# print(len(descendents))
# driver.close()
# #follwing
# followings=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/ancestor::tr/following::*")
# print(len(followings))
# driver.close()
#fallowing-sibling
# followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/ancestor::tr/following-sibling::*")
# print(len(followingsiblings))
# driver.close()
#precedings
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Financial Servic')]/ancestor::tr/preceding-sibling::*")
print(len(precedingsiblings))
driver.close()