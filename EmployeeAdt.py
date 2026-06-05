import time
import tracemalloc

class Employee:
    def __init__(self, name , desig , salary):
        self.name = name
        self.desig = desig
        self.salary = salary

    def read(self):
        self.name = input("Enter your name :")
        self.desig = input("Enter your desig :")
        self.salary = input("Enter your salary :")

    def display(self):
        print("Name :", self.name , "Designation :",self.desig, "Salary :",self.salary)

el = Employee('','',0)

start = time.process_time()
tracemalloc.start()

print('details of the employee')
el.read()
el.display()

print("space required :", tracemalloc.get_traced_memory())

end = time.process_time()

print("time requored :",(start-end))

tracemalloc.stop()