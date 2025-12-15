from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def find_login_button_smart(driver):
    """
    Self-healing locator стратеги
    """
    # Стратеги 1: ID-аар
    try:
        return driver.find_element(By.ID, "loginBtn")
    except NoSuchElementException:
        pass
    
    # Стратеги 2: Шинэ ID-аар
    try:
        return driver.find_element(By.ID, "signinButton")
    except NoSuchElementException:
        pass
    
    # Стратеги 3: Текстээр
    try:
        return driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    except NoSuchElementException:
        pass
    
    # Стратеги 4: Class-аар
    try:
        return driver.find_element(By.CLASS_NAME, "btn-primary")
    except NoSuchElementException:
        pass
    
    raise NoSuchElementException("Login button олдсонгүй")

def test_login_self_healing():
    driver = webdriver.Chrome()
    driver.get("file:///path/to/login_page.html")
    
    button = find_login_button_smart(driver)
    button.click()
    
    driver.quit()
