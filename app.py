from database import Database
from user import User
from student import Student
from pwinput import pwinput

def input_nonempty(prompt):
    x = input(prompt).strip()
    while not x:
        x = input(prompt).strip()
    return x

def input_nonempty_masked(prompt):
    x = pwinput(prompt).strip()
    while not x:
        x = pwinput(prompt).strip()
    return x

def auth_menu(db):
    u = User(db)
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            username = input_nonempty("Username: ")
            password = input_nonempty("Password: ")
            ok, msg = u.register(username, password)
            print(msg)
        elif choice == "2":
            username = input_nonempty("Username: ")
            password = input_nonempty_masked("Password: ")
            ok, user_id = u.login(username, password)
            if ok:
                print("Login successful")
                main_menu(db)
            else:
                print("Login failed")
        elif choice == "3":
            break
        else:
            print("Invalid")

def main_menu(db):
    s = Student(db)
    while True:
        print("\n1. Add student")
        print("2. Get student by ID")
        print("3. Update student")
        print("4. Delete student")
        print("5. View all students")
        print("6. Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input_nonempty("Name: ")
            dob = input_nonempty("DOB YYYY-MM-DD: ")
            course = input_nonempty("Course: ")
            email = input_nonempty("Email: ")
            new_id = s.add_student(name, dob, course, email)
            print(f"Student created with ID {new_id}")
        elif choice == "2":
            sid = input_nonempty("Student ID: ")
            try:
                sid_int = int(sid)
            except ValueError:
                print("Invalid ID")
                continue
            record = s.get_student_by_id(sid_int)
            if record:
                print(record.display_profile())
            else:
                print("Not found")
        elif choice == "3":
            sid = input_nonempty("Student ID: ")
            try:
                sid_int = int(sid)
            except ValueError:
                print("Invalid ID")
                continue
            dob = input_nonempty("New DOB YYYY-MM-DD: ")
            course = input_nonempty("New Course: ")
            email = input_nonempty("New Email: ")
            s.update_student(sid_int, dob, course, email)
            print("Updated")
        elif choice == "4":
            sid = input_nonempty("Student ID: ")
            try:
                sid_int = int(sid)
            except ValueError:
                print("Invalid ID")
                continue
            s.delete_student(sid_int)
            print("Deleted")
        elif choice == "5":
            records = s.get_all_students()
            if not records:
                print("No students")
            else:
                for rec in records:
                    print(rec.display_profile())
        elif choice == "6":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="NewPass123!", database="student_db")
    try:
        auth_menu(db)
    finally:
        db.close()
