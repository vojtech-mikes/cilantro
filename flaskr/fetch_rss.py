import pathlib
from bs4 import BeautifulSoup, Tag, ResultSet
from typing import cast
from models import RssObject, RssItems


def load_rss():
    rss_path = pathlib.Path("rss").absolute()

    with open(rss_path, "r") as f:
        data = BeautifulSoup(f, "xml")

    items = cast(ResultSet[Tag], data.find_all("item"))

    rss_items = []

    for item in items:
        rss_item = RssItems(
            title=item.title.text if item.title else "Title Not Found",
            link=item.link.text if item.link else "Link Not Found",
            pub_date=item.pubDate.text if item.pubDate else "Publish Date Not Found",
            desc=item.description.text if item.description else "Description Not Found",
        )
        rss_items.append(rss_item)

    rss_object = RssObject(
        items=rss_items if rss_items else [],
        link=data.link.text if data.link else "Link Not Found",
        title=data.title.text if data.title else "No Title Found",
        last_build_date=(
            data.lastBuildDate.text if data.lastBuildDate else "No Build Date Found"
        ),
    )

    return rss_object
