class Student:
    def __init__(self, name, age):
        self._name = name          # _name is a convention for "protected"
        self._age = age

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age with validation
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value


# Usage
s = Student("Mahesh", 25)

print(s.name)      # Output: Mahesh     → calls getter
print(s.age)       # Output: 25        → calls getter

s.name = "Rahul"   # → calls setter
s.age = 26         # → calls setter

print(s.name, s.age)