class programmer:
    company = "Microsoft"
    name = "___"
    age = 0
    position = "___"
    id = 0
    salary = 0.0
    def __init__(self, name, age, position, id, salary):
        self.name = name
        self.age = age
        self.position = position
        self.id = id
        self.salary = salary

harry = programmer("Harry", 24, "Developer", 1, 50000.0)
rohan = programmer("Rohan", 19, "Data Analyst", 2, 60000.0)
print(harry.company, harry.name,    harry.age, harry.position, harry.id, harry.salary)
print(rohan.company, rohan.name, rohan.age, rohan.position, rohan.id, rohan.salary)