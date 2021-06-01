import playsound
import os
from gtts import gTTS
from rich import print
from gnewsclient import gnewsclient


class Speak():
    def __init__(self, language):
        self.language = language
        self.location_voice = os.path.join("voice.mp3")

    def speak(self, text):
        tts = gTTS(text=text, lang=self.language)
        filename = self.location_voice
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)


class News():
    def __init__(self, language="english", location="United States", topic="World", no_of_news=10):
        self.language = language
        self.location = location
        self.topic = topic
        self.no_of_news = no_of_news

        self.client = gnewsclient.NewsClient(
            language=self.language,
            topic=self.topic,
            location=self.location,
            max_results=self.no_of_news
        )

    def get_news(self):
        self.news_all = self.client.get_news()
        self.results = []

        for news in self.news_all:
            self.results.append(news["title"])

        return self.results
