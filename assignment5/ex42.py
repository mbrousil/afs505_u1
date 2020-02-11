# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def make_noise(self):
            print("???")

Animal.make_noise("test")

# ??
class Dog(Animal):

    def __init__(self, name):
        # ??
        self.name = name

    def make_noise(self):
            print("bark")

Dog.make_noise("Fred")

# ??
class Cat(Animal):

    def __init__(self, name):
        # ??
        self.name = name
    def make_noise(self):
            print("meow")

# ??
class Person(object):

    def __init__(self, name):
        # ??
        self.name = name

        # Person has-a pet of some kind
        self.pet = None
    def make_noise(self):
            print("I like R more than Python")

# ??
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        self.info = {"salary":salary, "name": name}
        # ??
        self.salary = salary
    def make_noise(self):
            print("Listen, are you gonna have those TPS reports for us this afternoon?")

peter = Employee("Peter", 150000)
print(peter.info)

# ??
class Fish(object):
    pass

# ??
class Salmon(Fish):
    pass

# ??
class Halibut(Fish):
    pass

# Rover is-a Dog
rover = Dog("Rover")

# ??
satan = Cat("Satan")

# ??
mary = Person("Mary")

# ??
mary.pet = satan

# ??
frank = Employee("Frank", 120000)

# ??
frank.pet = rover

# ??
flipper = Fish()

# ??
crouse = Salmon()

# ??
harry = Halibut()
