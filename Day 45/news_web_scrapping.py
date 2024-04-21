from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_code = response.text

with open("demo.html", mode="w") as file:
    file.write(web_code)

soup = BeautifulSoup(web_code, "html.parser")
article_text = []
article_link = []
news_heading = soup.find_all(name="span", attrs={"class": "titleline"})
news_vote = soup.find_all(name="span", class_="score")
for span in news_heading:
    title = span.find("a").text
    link = span.find("a").get("href")
    article_text.append(title)
    article_link.append(link)
article_vote = [int(score.text.split(" ")[0]) for score in news_vote]


max_vote_index = article_vote.index(max(article_vote))
print(article_text[max_vote_index])
print(article_link[max_vote_index])
print(article_vote[max_vote_index])
print("Article No. :", max_vote_index + 1)
