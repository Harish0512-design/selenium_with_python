import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Test Case:
# Navigate to URL https://www.saucedemo.com/
# Enter username and Password
# Click Login
# verify user is login (Products title is present or not)
# click on logout
# verify user is logged out

# adding ChromeDriver path
service_obj = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# opening url on chrome browser
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# enter username, password and click on login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# verify products Title
products_title = driver.find_element(By.CSS_SELECTOR, "span.title").text
if products_title == "Products":
    print("User logged in Successfully")
else:
    print("User not logged in")

# verify sidebar button is present or not
# click on logout
# verify user logout
sidebar_btn = driver.find_element(By.ID, "react-burger-menu-btn")
if sidebar_btn.is_displayed():
    print("sidebar button is displayed")
    sidebar_btn.click()
    print("clicked on sidebar button")
    time.sleep(5)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    print("User Logged Out successfully")
else:
    print("User logout is not possible")

# quitting the driver
driver.quit()
