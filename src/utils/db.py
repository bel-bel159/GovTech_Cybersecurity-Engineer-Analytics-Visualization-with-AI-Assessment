from pathlib import Path
import sqlite3

# Path to the database file (inside src/output)
DB_PATH = Path(__file__).resolve().parents[1] / "output" / "sales_dw.sqlite"
SCHEMA_FILE = Path(__file__).resolve().parents[1] / "schema" / "schema.sql"


# Create and return a SQLite connection with foreign key support turned on.
def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


# This is to create all tables if they do not exist, and if they do exist, recreate all tables
def init_schema() -> None:
    DB_PATH.parent.mkdir(exist_ok=True)  # make sure output/ exists
    with get_connection() as conn, open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
