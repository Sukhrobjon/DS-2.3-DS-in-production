
# empCount is a class variable


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employee()

    @classmethod
    def num_employee(cls):
        cls.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


if __name__ == "__main__":

    # # "This would create first object of Employee class"
    # emp1 = Employee("Zara", 2000)
    # # "This would create second object of Employee class"
    # emp2 = Employee("Manni", 5000)
    # print("Total Employee %d" % Employee.empCount)

    def next_(n, x):
        return (x+n/x)/2

    n = 2
    # f = lambda x: next_(n, x)
    f = lambda x: (x+n/x)/2
    a_0 = 1.0

    print([round(x, 4) for x in (a_0, f(a_0))])
