from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_PHONE = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        continue_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        continue_button.click()

        time.sleep(3)

        go_btn = self.driver.find_element(
            By.XPATH,
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]",
        )
        go_btn.click()

        time.sleep(60)

        self.down = self.driver.find_element(
            By.XPATH,
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span",
        ).text
        self.up = self.driver.find_element(
            By.XPATH,
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span",
        ).text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(20)

        signin_btn = self.driver.find_element(
            By.XPATH,
            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        )
        signin_btn.send_keys(TWITTER_PHONE)

        next_btn = self.driver.find_element(
            By.XPATH,
            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span",
        )
        next_btn.click()

        time.sleep(10)

        password = self.driver.find_element(
            By.XPATH,
            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input",
        )
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up that?"
        post = self.driver.find_element(
            By.XPATH,
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div",
        )
        post.send_keys(tweet)
        time.sleep(20)

        post_btn = self.driver.find_element(
            By.XPATH,
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span",
        )
        post_btn.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
