from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
servobj=Service(r"C:\Users\Njoki Matheri\Downloads\chromedriver_win32\chromedriver")

driver=webdriver.Chrome(service=servobj)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(by=By.NAME,value="txtUsername").send_keys("Admin")
driver.find_element(by=By.ID,value="txtPassword").send_keys("admin123")
driver.find_element(by=By.CLASS_NAME,value="button").click()



actualtitle=driver.title
exptitle="OrangeHRM"
if exptitle==actualtitle:
    print("Test Login Passed")
else:
    print("Test Failed")

driver.close()