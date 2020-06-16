class Employee:
    total = 0 # total number of Employee
    salary = [] # list of the salary
    def __init__(self, first, last, salary, department): # creating instances
        self.first = first
        self.last = last
        self.salary = salary
        Employee.salary.append(salary) # storing the salary in a list so it can be accessed later
        self.department = department
        Employee.total = Employee.total + 1 # adding the number of the Employees
        print("Employee", first, last, "is added with the salary of", salary,"$ in department", department)
    def getAverage(self):
        totalSalary = 0
        for n in range(Employee.total): # loop total times to get the total Salary
            totalSalary = totalSalary + Employee.salary[n]
        return totalSalary/Employee.total # return the average Salary
class fullTimeEmployee(Employee):
    def __inut__(self, first, last, salary, department):
        Employee.__init__(self, first, last, salary, department) # calling Employee __init__

A = Employee("Anh", "Nguyen", 1000, "A")
print("The average salary now is:", A.getAverage())
B = fullTimeEmployee("B", "B", 2000, "B")
print("The average salary now is:", B.getAverage())
C = fullTimeEmployee("C", "C", 3000, "C")
print("The average salary now is:", C.getAverage())