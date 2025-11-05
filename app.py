from pwinput import pwinput
from database import Database
from user import User
from student import Student

def input_nonempty(prompt):
    x = input(prompt).strip()
    while not x:
        x = input(prompt).strip()
    return x

def input_int(prompt):
    while True:
        x = input(prompt).strip()
        if x.isdigit():
            return int(x)
        print("Enter a number")

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
            password = pwinput(prompt="Password: ", mask="*")
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
            sid = input_int("Student ID: ")
            row = s.get_student_by_id(sid)
            if row:
                print(f"{row['id']} | {row['name']} | {row['dob']} | {row['course']} | {row['email']}")
            else:
                print("Not found")
        elif choice == "3":
            sid = input_int("Student ID: ")
            dob = input_nonempty("New DOB YYYY-MM-DD: ")
            course = input_nonempty("New Course: ")
            email = input_nonempty("New Email: ")
            s.update_student(sid, dob, course, email)
            print("Updated")
        elif choice == "4":
            sid = input_int("Student ID: ")
            confirm = input("Type YES to delete: ").strip()
            if confirm == "YES":
                s.delete_student(sid)
                print("Deleted")
            else:
                print("Cancelled")
        elif choice == "5":
            rows = s.get_all_students()
            if not rows:
                print("No students")
            else:
                for r in rows:
                    print(f"{r['id']} | {r['name']} | {r['dob']} | {r['course']} | {r['email']}")
        elif choice == "6":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    db = Database(host="localhost", port=3307, user="root", password="toor", database="student_db")
    try:
        auth_menu(db)
    finally:
        db.close()
