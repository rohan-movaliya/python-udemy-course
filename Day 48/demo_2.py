from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.python.org/")

events_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for i in range(len(events_time)):
    events[i] = {"time": events_time[i].text, "name": events_name[i].text}
print(events)


driver.close()
