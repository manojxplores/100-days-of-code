from bs4 import BeautifulSoup
import requests

res = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = res.text

soup = BeautifulSoup(contents, "html.parser")

movies_list = []
all_divs = soup.find_all(name="div", class_="article-title-description__text")
for div in all_divs:
    movies_list.append(div.h3.getText())

movies_list.reverse()

with open("movies.txt", mode="a", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
