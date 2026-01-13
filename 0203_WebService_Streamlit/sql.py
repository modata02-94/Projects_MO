import sqlite3
from datetime import datetime

DB_NAME = "weather.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            weather_de TEXT,
            weather_en TEXT,
            timestamp TEXT       
        )
    """)

    conn.commit()
    conn.close()


def insert_weather(city, temperature, weather_de, weather_en):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather (city, temperature, weather_de, weather_en, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        city,
        temperature,
        weather_de,
        weather_en,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()
