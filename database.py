import sqlite3
import os

# Railway'da /data, VS Code'da loyiha papkasi
if os.path.exists("/data"):
    DB_PATH = "/data/users.db"
else:
    DB_PATH = "users.db"

db = sqlite3.connect(DB_PATH)
sql = db.cursor()