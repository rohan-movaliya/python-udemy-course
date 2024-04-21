import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_web_code = response.text

soup = BeautifulSoup(movie_web_code, "html.parser")
movie_title = soup.find_all(name="h3", class_="title")
all_movie = [movie.getText() for movie in movie_title][::-1]

with open("movie.txt", mode="w", encoding="utf-8") as file:
    for movie in all_movie:
        file.write(f"{movie}\n")
