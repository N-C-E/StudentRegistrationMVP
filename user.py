import hashlib

class User:
    def __init__(self, db):
        self.db = db

    def register(self, username, password):
        existing = self.db.fetchone("SELECT id FROM users WHERE username=%s", (username,))
        if existing:
            return False, "Username taken"
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.db.execute("INSERT INTO users (username, password_hash) VALUES (%s,%s)", (username, hashed))
        return True, "Registered"

    def login(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        row = self.db.fetchone("SELECT id FROM users WHERE username=%s AND password_hash=%s", (username, hashed))
        if row:
            return True, row["id"]
        return False, None
