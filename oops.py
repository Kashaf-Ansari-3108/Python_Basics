class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def getSalary(self):
         print(self.salary)



rohan = Employee("Rohan", '3455')
# print(rohan.salary)
# print(rohan.name)
rohan.getSalary()

kashaf = Employee("Kashaf", '34500000')
# print(kashaf.salary)
# print(kashaf.name)
kashaf.getSalary()
