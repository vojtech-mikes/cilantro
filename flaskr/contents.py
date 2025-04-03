from urllib.request import urlretrieve
from flaskr.constants import TMP_CONTENT_PATH
from xml.etree import ElementTree


def parse_contents(record: str) -> dict:
    urlretrieve(record, TMP_CONTENT_PATH)

    content_tree = ElementTree.parse(TMP_CONTENT_PATH)
