import requests
from bs4 import BeautifulSoup

url = "https://goutezlebulgare.com/"
reponse = requests.get(url)


if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html.parser")
    title = soup.find("h1")

    print(title.text)
