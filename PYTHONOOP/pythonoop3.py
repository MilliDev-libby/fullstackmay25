# Parent Class
class Pearson:
    def __init__(self, name, id_number): 
        self.name = name
        self.id_number = id_number
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
    
# Child Class
class Employee(Pearson):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post

    def display(self):
        super().display()
        print(f"Salary: ${self.salary}")
        print(f"Post: {self.post}")
    
# Create Pearson object 
person1 = Pearson("Alice Johnson", "P12345")

# Create Employee object
employee1 = Employee("Bob Smith", "E67890", 75000, "Software Engineer")

# Display information
print("Print Info:")
person1.display()

print("/nEmployee Info:")
employee1.display()

