from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_traditional():
    driver = webdriver.Chrome()
    driver.get("/Users/javkhaa/code/F.CSA313_LAB15/ui_demo.html")
    
    driver.find_element(By.ID, "loginBtn").click()
    
    time.sleep(2)
    driver.quit()
