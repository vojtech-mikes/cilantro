from dataclasses import dataclass
from typing import List


@dataclass
class RssItems:
    title: str
    link: str
    pub_date: str
    desc: str


@dataclass
class RssObject:
    title: str
    link: str
    last_build_date: str
    items: List[RssItems]
