import hashlib

class User:
    def __init__(self, db):
        self.db = db

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        exists = self.db.fetchone("SELECT id FROM users WHERE username=%s", (username,))
        if exists:
            return False, "Username taken"
        hashed = self.hash_password(password)
        self.db.execute("INSERT INTO users (username, password_hash) VALUES (%s,%s)", (username, hashed))
        return True, "Registered"

    def login(self, username, password):
        hashed = self.hash_password(password)
        row = self.db.fetchone("SELECT id FROM users WHERE username=%s AND password_hash=%s", (username, hashed))
        if row:
            return True, row["id"]
        return False, None
