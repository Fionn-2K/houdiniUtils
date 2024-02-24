class Base:
        def __init__(self):
                self.a = "test"
                self._b = "test2"
                self.__c = "test3"

class Derived(Base):
        def __init__(self):
            Base.__init__(self)
            print("Calling base")
            print(self.a)
            print(self._b)
            print(self.__c) ## with cause error. __c it private to the parent class Base()

test1 = Base()
print(test1.a)

test2 = Derived()