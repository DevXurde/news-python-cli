from scripts.speak import Speak
from scripts.news import News
import click
from rich import print

language_support = (
    ("english", "en"),
    ("hindi", "hi"),
    ("french", "fr"),
    ("spanish", "es"),
    ("mandarin-china", "zh-CN"),
    ("mandarin-taiwan", "zh-TW"),
    ("portugese", "pt")
)


@click.command()
@click.option(
    "--language",
    default="english",
    help="It takes the language of your choice", type=str,
    required=False
)
@click.option(
    "--topic",
    default="Top Stories",
    help="It takes the topic of your choice", type=str,
    required=False
)
@click.option(
    "--location",
    default="United States",
    help="It takes the location of your choice", type=str,
    required=False
)
def cli(language, topic, location):

    news_language = str(language)
    news_topic = str(topic)
    news_location = str(location)

    news_client = News(
        language=news_language,
        topic=news_topic,
        location=news_location
    )

    news = news_client.get_news()

    print(
        f"\n[bold green]Showing in [/bold green][bold blue]{news_language.capitalize()}[/bold blue]")
    print(
        f"[bold green]From [/bold green][bold blue]{news_location}[/bold blue]")
    print(
        f"[bold green]Topic : [/bold green][bold blue]{news_topic}[/bold blue]")

    for language_name, language_code in language_support:
        language = language.replace(language_name, language_code)
        speak = Speak(language=language)

    if news:
        for i in range(len(news)):
            print(f"\n[bold red]{i + 1}.[bold red]", end=" ")
            speak.speak(news[i], color="red")

    else:
        print(
            f"\n[bold red]Sorry I Dont think there are any news in the language [bold blue]{news_language.capitalize()}[/bold blue] , from location [bold blue]{news_location}[/bold blue] and on topic [bold blue]{news_topic}[bold blue].[/bold red]\n"
        )


if __name__ == "__main__":
    cli()
