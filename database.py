import sqlite3
from datetime import datetime

class StoryDB:
    def __init__(self, db_name="chronicle.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS prompt_versions 
                          (id INTEGER PRIMARY KEY, scene_id INTEGER, version INTEGER, 
                           prompt_text TEXT, created_at TEXT)''')
        self.conn.commit()

    def save_version(self, scene_id, prompt):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(version) FROM prompt_versions WHERE scene_id = ?", (scene_id,))
        result = cursor.fetchone()[0]
        new_version = (result + 1) if result is not None else 1
        
        cursor.execute('''INSERT INTO prompt_versions (scene_id, version, prompt_text, created_at)
                          VALUES (?, ?, ?, ?)''', 
                       (scene_id, new_version, prompt, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.conn.commit()
        return new_version

    def get_versions(self, scene_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT version, prompt_text, created_at FROM prompt_versions WHERE scene_id = ? ORDER BY version DESC", (scene_id,))
        return cursor.fetchall()