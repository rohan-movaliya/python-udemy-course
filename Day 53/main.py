from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,gu;q=0.7",
}
print("------Data Gathering------")
response = requests.get("https://silveroakuni.ac.in/", headers=header)
data = response.text

soup = BeautifulSoup(data, "html.parser")

all_heading_elements = soup.select("#ul_circular li a p ")
all_heading = []
for heading in all_heading_elements:
    all_heading.append(heading.string)

all_link_elements = soup.select("#ul_circular li a ")
all_link = []
for link in all_link_elements:
    href = link["href"]
    all_link.append(href)


driver = webdriver.Chrome()

time.sleep(2)
for i in range(7):
    driver.get("<FORM LINK>")

    time.sleep(2)
    circular = driver.find_element(
        By.XPATH,
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    link_of_circular = driver.find_element(
        By.XPATH,
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    submit_btn = driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span"
    )

    circular.send_keys(all_heading[i])
    link_of_circular.send_keys(all_link[i])
    submit_btn.click()
