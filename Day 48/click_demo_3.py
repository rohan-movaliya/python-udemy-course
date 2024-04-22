from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_article = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# total_article.click()

view_source = driver.find_element(By.LINK_TEXT, "View source")
# view_source.click()

search = driver.find_element(By.NAME, "search")
sleep(5)

search.send_keys("Python Programming")

search.send_keys(Keys.ENTER)

sleep(5)
driver.quit()
