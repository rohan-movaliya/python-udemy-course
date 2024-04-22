from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Rohan")
sleep(5)
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Movaliya")
sleep(5)
email = driver.find_element(By.NAME, "email")
email.send_keys("rohanmovaliya64@gmail.com")
sleep(5)
signup_button = driver.find_element(By.TAG_NAME, "button")
signup_button.click()
sleep(5)
