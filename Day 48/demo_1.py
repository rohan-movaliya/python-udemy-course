from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome()
driver.get(
    "https://www.amazon.in/iQOO-Stellar-Snapdragon-Segment-Included/dp/B07WHSR1NR/?_encoding=UTF8&ref_=dlx_gate_sd_dcl_tlt_e2483f9e_dt_pd_gw_unk&pd_rd_w=6ld1L&content-id=amzn1.sym.9e4ae409-2145-4395-aa6e-45d7f3e95c3e&pf_rd_p=9e4ae409-2145-4395-aa6e-45d7f3e95c3e&pf_rd_r=P6MJQPMADBPMKSRVNAKQ&pd_rd_wg=gTNet&pd_rd_r=b7bc8ef5-3a33-4f9e-9d5d-9ca2642ee13f&th=1"
)

ratigs = driver.find_element(By.ID, "acrCustomerReviewText")
price = driver.find_element(
    By.XPATH,
    "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[3]/span[2]/span[2]",
)
print(price.text)
print(ratigs.text)
print(ratigs.tag_name)
print(ratigs.get_attribute("class"))
