from twilio.rest import Client
import requests

STOCK_API_KEY = ""
NEWS_API_KEY = ""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = round(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percentage = (difference / float(yesterday_closing_price)) * 100

if abs(diff_percentage) > 1:
    news_params = {"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME}
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articales = [
        f"{STOCK_NAME} : {up_down} {diff_percentage}%\nHeadline: {article['title']}. \n Brief: {article['description']}"
        for article in three_articles
    ]

    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    formatted_articales = [1, 2, 3]
    for article in formatted_articales:
        message = client.messages.create(body=article, from_="", to="")
