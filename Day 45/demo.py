from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")    # Alternative Way

# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)

# print(soup.h1.string) #first searched

# print(soup)
# print(soup.prettify()) #for formatted

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h2", class_ = "heading")
# print(section_heading.get("class"))

collage_url = soup.select_one(selector="p a")
print(collage_url)

name = soup.select_one(selector="#name")
print(name)

name = soup.select_one(selector="#name")
print(name)

study = soup.select(selector=".study")
print(study)
