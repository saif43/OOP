class Worker:
    def __init__(self, name, position,salary):
        self.name = name
        self.position = position
        self.salary = salary


saif = Worker("Saif","Back-End Developer",50000)
zahid = Worker("Zahid","Back-End Developer",50000)

print(saif.name)
print(saif.position)
print(saif.salary)

print(zahid.name)
print(zahid.position)
print(zahid.salary)