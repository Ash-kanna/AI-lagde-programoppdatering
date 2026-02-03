import sqlite3
import requests
from datetime import datetime

DB_FILE = 'vlc_updates.db'
PRODUCT = 'vlc'
GITHUB_API_URL = 'https://api.github.com/repos/videolan/vlc/releases/latest'

def get_latest_version():
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        data = response.json()
        return data['tag_name']
    except Exception as e:
        print(f"Feil ved henting av siste versjon: {e}")
        return None

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS versions
                 (id INTEGER PRIMARY KEY, product TEXT UNIQUE, version TEXT, last_check TEXT)''')
    conn.commit()
    conn.close()

def get_stored_version():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT version FROM versions WHERE product=?", (PRODUCT,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def update_version(version):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    now = datetime.now().isoformat()
    c.execute("INSERT OR REPLACE INTO versions (product, version, last_check) VALUES (?, ?, ?)", (PRODUCT, version, now))
    conn.commit()
    conn.close()

def main():
    init_db()
    latest = get_latest_version()
    if latest is None:
        return
    stored = get_stored_version()
    if stored != latest:
        print(f"Ny versjon tilgjengelig: {latest}")
        update_version(latest)
    else:
        print("VLC er oppdatert til siste versjon.")
    # Oppdater alltid last_check
    update_version(latest)

if __name__ == "__main__":
    main()