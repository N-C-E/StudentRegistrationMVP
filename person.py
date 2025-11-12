class Person:
    def __init__(self, name: str, dob: str, email: str) -> None:
        self.name = name
        self.dob = dob
        self.email = email

    def display_profile(self) -> str:
        return f"Name: {self.name}, DOB: {self.dob}, Email: {self.email}"