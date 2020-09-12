from app.ms_azure_rss import get_azure_articles


def main() -> None:
    articles = get_azure_articles()
    for article in articles:
        print(article)


if __name__ == "__main__":
    main()
