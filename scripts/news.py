from gnewsclient import gnewsclient


class News():
    def __init__(self, language="english", location="United States", topic="World"):
        self.language = language
        self.location = location
        self.topic = topic

        self.client = gnewsclient.NewsClient(
            language=self.language,
            topic=self.topic,
            location=self.location
        )

    def get_news(self):
        self.news_all = self.client.get_news()
        self.results = []

        for news in self.news_all:
            self.results.append(news["title"])

        return self.results
