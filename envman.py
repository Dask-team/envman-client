import sqlite3
from typing import Optional

import dotenv
import typer
from rich import print
import json

app = typer.Typer(
    name="envman",
    help="A simple CLI tool to manage environment variables"
)


@app.command()
def init(dotenv: Optional[str] = ".env", db: Optional[str] = "env.db"):
    # check if already initialized
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM env")
        print("Already initialized")
        return
    except sqlite3.OperationalError:
        pass

    # create table: env table - uuid, key, value / changelog table - uuid, key, value, action, timestamp
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE env (uuid TEXT PRIMARY KEY, key TEXT, value TEXT)")
    cursor.execute("CREATE TABLE changelog (uuid TEXT PRIMARY KEY, key TEXT, value TEXT, action TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()

    # make dotenv file
    with open(dotenv, "w") as f:
        f.write("")

    # save dotenv file name and db name to envmanifest.json


    print("Initialized successfully")


@app.command()
def add(key: str, value: str, db: Optional[str] = "env.db"):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO env (uuid, key, value) VALUES (?, ?, ?)", (key, key, value))
    cursor.execute("INSERT INTO changelog (uuid, key, value, action, timestamp) VALUES (?, ?, ?, ?, datetime('now'))",
                   (key, key, value, "add"))
    conn.commit()
    conn.close()

    # add to dotenv file
    dotenv.set_key(".env", key, value)

    print(f"Added {key}={value} successfully")


if __name__ == "__main__":
    app()
