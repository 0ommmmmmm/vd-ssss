class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name   = name
        self.rollno = rollno
        self.m1     = m1
        self.m2     = m2

    def __str__(self):
        return f"Name: {self.name} | Roll: {self.rollno} | M1: {self.m1} | M2: {self.m2}"


students = []

def accept(name, rollno, m1, m2):
    students.append(Student(name, rollno, m1, m2))

def display_all():
    for s in students:
        print(s)

def search(rollno):
    for i, s in enumerate(students):
        if s.rollno == rollno:
            return i
    return -1

def delete(rollno):
    i = search(rollno)
    if i != -1:
        del students[i]

def update(rollno, new_rollno):
    i = search(rollno)
    if i != -1:
        students[i].rollno = new_rollno


# --- Run ---
accept("A", 1, 100, 100)
accept("B", 2, 90, 90)
accept("C", 3, 80, 80)

print("All Students:")
display_all()

print("\nSearch Roll 2:")
i = search(2)
print(students[i])

delete(2)
print("\nAfter Delete:")
display_all()

update(3, 99)
print("\nAfter Update:")
display_all()