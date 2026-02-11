import requests
import sqlite3
from datetime import datetime

INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

INDEXNOW_KEY = "adrock-indexnow-2026"
KEY_LOCATION = "https://mobiledelivery.com.br/indexnow/adrock-indexnow-2026.txt"
HOST = "mobiledelivery.com.br"

DB_PATH = "indexnow/logs.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            status INTEGER,
            response TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def already_sent(url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM submissions WHERE url = ?", (url,))
    result = cursor.fetchone()

    conn.close()

    return result is not None


def send_urls(urls):
    urls_to_send = []

    for url in urls:
        if not already_sent(url):
            urls_to_send.append(url)

    if not urls_to_send:
        print("Nenhuma URL nova para enviar.")
        return None

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls_to_send
    }

    response = requests.post(INDEXNOW_ENDPOINT, json=payload)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for url in urls_to_send:
        cursor.execute("""
            INSERT INTO submissions (url, status, response, created_at)
            VALUES (?, ?, ?, ?)
        """, (url, response.status_code, response.text, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()

    print(f"Enviado {len(urls_to_send)} URLs. Status: {response.status_code}")

    return response.status_code