class Employee:
        def __init__(self, first_name, last_name, age, role) -> None:
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.role = role

        @property ## @property makes the method a property like self.first_name [GETTER]
        def full_name(self):
            return self.first_name + " " + self.last_name

        @full_name.setter ## [SETTER]
        def full_name(self, value):
            first, last = value.split()
            self.first_name = first
            self.last_name = last

        @full_name.deleter ## [DELETER]
        def full_name(self):
            del self.first_name

        @property
        def email(self):
            return self.first_name + "." + self.last_name + "@email.com"

        @email.setter
        def email(self, value):
            value1, value2 = value.split()
            return value1 + "." + value2 + "@email.com"


em = Employee("Bob", "Something", 21, "Junior Artist")
em.full_name = "Amy SomethingElse"
print(em.full_name)
print(em.email)