import time
import tracemalloc

# Employee class
class Employee:

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    # Input employee details
    def read(self):
        self.name = input("Enter name: ")
        self.designation = input("Enter designation: ")
        self.salary = int(input("Enter salary: "))

    # Display employee details
    def display(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
        print()

# Start time and memory tracking
start = time.process_time()
tracemalloc.start()

employees = []

# Input loop
while True:
    emp = Employee("", "", 0)
    emp.read()

    employees.append(emp)

    choice = input("Add more employees? (y/n): ")

    if choice == 'n':
        break

# Display all employees
print("\nEmployee Details:\n")

for emp in employees:
    emp.display()

# End time
end = time.process_time()

# Space and time complexity
print("Memory Used:", tracemalloc.get_traced_memory())
print("Time Taken:", end - start)
tracemalloc.stop()

