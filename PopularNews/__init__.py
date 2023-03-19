import requests
from bs4 import BeautifulSoup


class NewsScraper:
    def __init__(self, url):
        self.description = "This app show top 5 news in Indonesia based from detik.com"
        self.result = None
        self.url = url

    def data_extraction(self):
        content = requests.get(self.url)
        soup = BeautifulSoup(content.text, "html.parser")
        top5 = soup.find("div", {"class": "box cb-mostpop"})
        titles = []
        for article in top5.find_all("article"):
            title = article.find("h3", class_="media__title").find("a").text.strip()
            titles.append(title)

        urls = []
        for article in top5.find_all("article"):
            url = article.find("h3", class_="media__title").find("a")
            urls.append(url.get("href"))

        hasil = dict()
        hasil["Titles"] = titles
        hasil["Urls"] = urls
        return hasil

    def data_displaying(self):
        print("Berita Terpopuler!")
        result = self.data_extraction()
        for i in range(0, 5):
            print(f'{i+1}. {result["Titles"][i]}')
            print(f'Link: {result["Urls"][1]}')

    def run(self):
        self.data_extraction()
        self.data_displaying()


if __name__ == "__main__":
    DetikNewsScraper = NewsScraper("https://detik.com/")
    print(DetikNewsScraper.description)
    DetikNewsScraper.run()
    # print(description)
    # result = data_extraction()
    # data_displaying(result)
