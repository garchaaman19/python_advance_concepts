class Parent:
    # def __init__(self, name):
    #     self.name = name

    def greet(self):
        print(f"Hello, {self.name} from the Parent class!")

class Child(Parent):
    def __init__(self, name, age):
        # Using super() to call the parent class constructor
        # super().__init__(name)
        self.age = age
        self.name=name

    def greet(self):
        # Overriding the greet method but still using super()
        super().greet()  # Calls Parent's greet method
        print(f"You are {self.age} years old, from the Child class!")

# Example Usage
c = Child("Harvindar", 27)
c.greet()
