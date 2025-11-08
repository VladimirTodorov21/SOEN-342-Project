from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH  = BASE_DIR / "database" / "soen342project.db"

print("Expected DB path:", DB_PATH)
print("Exists:", DB_PATH.exists())