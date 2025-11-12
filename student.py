from typing import List, Optional

from person import Person


class StudentRecord(Person):
    def __init__(self, student_id: int, name: str, dob: str, course: str, email: str) -> None:
        super().__init__(name, dob, email)
        self.student_id = student_id
        self.course = course

    def display_profile(self) -> str:
        return (
            f"Student ID: {self.student_id}, Name: {self.name}, DOB: {self.dob}, "
            f"Course: {self.course}, Email: {self.email}"
        )


class Student:
    def __init__(self, db):
        self.db = db

    def add_student(self, name: str, dob: str, course: str, email: str) -> int:
        self.db.execute(
            "INSERT INTO students (name, dob, course, email) VALUES (%s,%s,%s,%s)",
            (name, dob, course, email),
        )
        row = self.db.fetchone("SELECT LAST_INSERT_ID() AS id")
        return row["id"]

    def get_student_by_id(self, student_id: int) -> Optional[StudentRecord]:
        row = self.db.fetchone("SELECT * FROM students WHERE id=%s", (student_id,))
        if not row:
            return None
        return StudentRecord(
            student_id=row["id"],
            name=row["name"],
            dob=str(row["dob"]),
            course=row["course"],
            email=row["email"],
        )

    def update_student(self, student_id: int, dob: str, course: str, email: str) -> bool:
        self.db.execute(
            "UPDATE students SET dob=%s, course=%s, email=%s WHERE id=%s",
            (dob, course, email, student_id),
        )
        return True

    def delete_student(self, student_id: int) -> bool:
        self.db.execute("DELETE FROM students WHERE id=%s", (student_id,))
        return True

    def get_all_students(self) -> List[StudentRecord]:
        rows = self.db.fetchall("SELECT * FROM students ORDER BY id")
        records: List[StudentRecord] = []
        for row in rows:
            records.append(
                StudentRecord(
                    student_id=row["id"],
                    name=row["name"],
                    dob=str(row["dob"]),
                    course=row["course"],
                    email=row["email"],
                )
            )
        return records
