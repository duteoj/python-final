import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print()
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
                print(f"Data loaded successfully: {len(self.students)} students")
                return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview_data(self, n=5):
        if not self.students:
            return
        print()
        print(f"First {n} rows:")
        print("-" * 30)
        for row in self.students[:n]:
            sid     = row['student_id']
            age     = row['age']
            gender  = row['gender']
            country = row['country']
            gpa     = row['GPA']
            print(f"{sid} | {age} | {gender} | {country} | GPA: {gpa}")
        print("-" * 30)
