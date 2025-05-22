import os
import sqlite3
from typing import List, Tuple


def _get_db_cursor() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    os.makedirs("db", exist_ok=True)
    sqlite_cnx = sqlite3.connect("db/cilantro.db")

    return sqlite_cnx, sqlite_cnx.cursor()


def table_init_check() -> None:
    conn, cursor = _get_db_cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS feeds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE NOT NULL
    )
    """
    )

    conn.commit()
    cursor.close()
    conn.close()


def load_saved_urls() -> List[str]:
    conn, cursor = _get_db_cursor()

    cursor.execute(
        """
    SELECT url FROM feeds
    """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return [x[0] for x in result]


def create_record(url: str) -> None:
    conn, cursor = _get_db_cursor()

    cursor.execute(
        """
    INSERT INTO feeds (url) VALUES (?)
    """,
        (url,),
    )

    conn.commit()
    cursor.close()
    conn.close()


def remove_record(url: str) -> None:
    conn, cursor = _get_db_cursor()

    cursor.execute(
        """
    DELETE FROM feeds WHERE url=(?)
    """,
        (url,),
    )

    conn.commit()
    cursor.close()
    conn.close()
