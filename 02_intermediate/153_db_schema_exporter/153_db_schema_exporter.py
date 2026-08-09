"""
Project 153: DB Schema Exporter
Category: Web & APIs
Description: SQLite relational database engine supporting schema initialization, CRUD transactions, and data querying.
"""
import sqlite3

class SQLiteEngine153:
    def __init__(self, db_name=":memory:"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_record(self, item, cat, amount):
        self.cursor.execute("INSERT INTO records (item, category, amount) VALUES (?, ?, ?)", (item, cat, amount))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_records(self):
        self.cursor.execute("SELECT * FROM records")
        return self.cursor.fetchall()

    def get_summary(self):
        self.cursor.execute("SELECT category, SUM(amount), COUNT(*) FROM records GROUP BY category")
        return self.cursor.fetchall()

def run_project_153():
    print("=" * 45)
    print("   PYTHON PROJECT 153: DB SCHEMA EXPORTER")
    print("=" * 45)
    
    db = SQLiteEngine153()
    db.add_record("Server Hosting", "Infrastructure", 49.99)
    db.add_record("Domain Name", "Infrastructure", 12.50)
    db.add_record("Team Lunch", "Perks", 85.00)
    
    print("\nInserted 3 SQLite Records:")
    records = db.get_all_records()
    for r in records:
        print(f"  ID: {r[0]} | Item: {r[1]} | Category: {r[2]} | Amount: ${r[3]:.2f}")
        
    print("\nCategory Aggregate Summary:")
    summary = db.get_summary()
    for cat, total, cnt in summary:
        print(f"  Category: {cat} | Total: ${total:.2f} | Count: {cnt}")
    return True

if __name__ == "__main__":
    run_project_153()
