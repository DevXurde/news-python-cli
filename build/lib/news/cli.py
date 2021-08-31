from news import News, Speak
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
    help="It takes the language of your choice",
    type=str,
    required=False
)
@click.option(
    "--topic",
    default="World",
    help="It takes the topic of your choice",
    type=str,
    required=False
)
@click.option(
    "--location",
    default="United States",
    help="It takes the location of your choice",
    type=str,
    required=False
)
@click.option(
    "--number",
    default=10,
    help="It takes the amount/number of news you want to see",
    type=int,
    required=False
)
def cli(language, topic, location, number):

    news_language = str(language)
    news_topic = str(topic)
    news_location = str(location)
    no_of_news = int(number)

    try:

        news_client = News(
            language=news_language,
            topic=news_topic,
            location=news_location,
            no_of_news=no_of_news,
        )

        news = news_client.get_news()

        sources = []

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
                new_news = news[i].split("- ")

                print(f"\n[bold red]{i + 1}.[bold red]", end=" ")
                print(f"[bold magenta]{new_news[0]}[/ bold magenta]")
                speak.speak(new_news[0])

                sources.append(new_news[1])

            print("\n[bold blue]Sources : [/bold blue]")
            for source in sources:
                print(f"[bold green]{source}[bold green]")

            print(f"\n[bold magenta]Thank You[/bold magenta]\n")
            speak.speak("Thank You")

        else:
            print(
                f"\n[bold red]Sorry I Dont think there are any news in the language [bold blue]{news_language.capitalize()}[/bold blue] , from location [bold blue]{news_location}[/bold blue] and on topic [bold blue]{news_topic}[bold blue].[/bold red]\n"
            )

    except:
        print(
            f"\n[bold red]Sorry Something Went Wrong, Please check your internet connection.[bold red]\n")


if __name__ == "__main__":
    cli()
