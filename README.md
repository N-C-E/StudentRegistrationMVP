## How to Run

1. Make sure MySQL and MySQL Workbench are installed on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run these commands one by one in order:

```
python -m venv venv
```
```
venv\Scripts\activate
```
```
python -m pip install --upgrade pip
```
```
pip install mysql-connector-python pwinput python-dotenv
```
```
python -m pip freeze > requirements.txt
```
```
python app.py
```
# Open MySQL Workbench, then:
1. File → Open SQL Script → select 'student_db.sql'
2. Click the lightning ⚡ button to run it
# Update these credentials inside app.py before running
```
db = Database(host="localhost", user="root", password="toor", database="student_db")
```
```
python app.py
```
## Show in MySQL
```
select * FROM users;
```
```
select * FROM students;
```

