class Student:
    def __init__(self, db):
        self.db = db

    def add_student(self, name, dob, course, email):
        self.db.execute("INSERT INTO students (name, dob, course, email) VALUES (%s,%s,%s,%s)", (name, dob, course, email))
        row = self.db.fetchone("SELECT LAST_INSERT_ID() AS id")
        return row["id"]

    def get_student_by_id(self, student_id):
        return self.db.fetchone("SELECT * FROM students WHERE id=%s", (student_id,))

    def update_student(self, student_id, dob, course, email):
        self.db.execute("UPDATE students SET dob=%s, course=%s, email=%s WHERE id=%s", (dob, course, email, student_id))
        return True

    def delete_student(self, student_id):
        self.db.execute("DELETE FROM students WHERE id=%s", (student_id,))
        return True

    def get_all_students(self):
        return self.db.fetchall("SELECT * FROM students ORDER BY id")
