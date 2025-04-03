from pathlib import Path
from flaskr.constants import DATA_PATH
from flaskr.tools import create_datafile


def create_records(form_data: dict) -> str:
    if not Path(DATA_PATH).exists():
        create_datafile()

    source = form_data["rss_source"]
    with open(DATA_PATH, "a") as f:
        f.write(source)
        f.write("\n")

    return source


def get_records() -> list:
    if not Path(DATA_PATH).exists():
        return []

    records = []

    with open(DATA_PATH) as f:
        for source in f:
            records.append(source.strip("\n"))

    return records


def delete_records(record: str) -> None:
    records = get_records()

    with open(DATA_PATH, "w") as f:
        for i in records:
            if i != record:
                f.write(i)
