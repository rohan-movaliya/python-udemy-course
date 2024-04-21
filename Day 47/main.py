import requests
import lxml
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = ""
auth_token = ""

url = "https://www.amazon.in/iQOO-Stellar-Snapdragon-Segment-Included/dp/B07WHSR1NR/?_encoding=UTF8&ref_=dlx_gate_sd_dcl_tlt_e2483f9e_dt_pd_gw_unk&pd_rd_w=6ld1L&content-id=amzn1.sym.9e4ae409-2145-4395-aa6e-45d7f3e95c3e&pf_rd_p=9e4ae409-2145-4395-aa6e-45d7f3e95c3e&pf_rd_r=P6MJQPMADBPMKSRVNAKQ&pd_rd_wg=gTNet&pd_rd_r=b7bc8ef5-3a33-4f9e-9d5d-9ca2642ee13f&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,gu;q=0.7",
}
BUY_PRICE = 10000.00
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency.replace(",", ""))

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+12514511098",
        body=f"Amazon Price Alert!\n\n{message}\n{url}",
        to="+917698979159",
    )

    print(message.sid)
