from typing import List
import feedparser
import dataclasses

from datetime import datetime


@dataclasses.dataclass(frozen=True)
class AzureArticle:
    id: str
    link: str
    title: str
    published: datetime
    summary: str
    tags: List[str]

    def __str__(self) -> str:
        return f"[{self.published}]  {self.title}"


def get_azure_articles() -> List[AzureArticle]:
    url = "https://azurecomcdn.azureedge.net/ja-jp/updates/feed/"
    res = feedparser.parse(url)
    entries = res["entries"]
    articles: List[AzureArticle] = list()
    for entry in entries:

        tags: List[str] = list()
        tags_dict = entry.get("tags", None)

        if tags_dict is not None:
            for tag_dict in tags_dict:
                tag_term = tag_dict.get("term", None)
                if tag_term is not None and isinstance(tag_term, str):
                    tags.append(tag_term)

        format = "%a, %d %b %Y %H:%M:%S Z"
        published = datetime.strptime(str(entry.get("published", "")), format)
        articles.append(
            AzureArticle(
                id=str(entry.get("id", "")),
                link=str(entry.get("link", "")),
                tags=tags,
                title=str(entry.get("title", "")),
                published=published,
                summary=str(entry.get("summary", "")),
            )
        )

    return articles
