from typing import Any


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("inside new")
        instance = super().__new__(cls)
        # Here we are calling the parent object's super i.e
        # super().__new__(cls) ensures that the parent class’s (usually object) __new__ method is invoked.
        # The parent’s __new__ method does the low-level work of allocating memory and setting up the new instance.
        # Without this call, the instance creation process would be incomplete, leading to issues.
        # try commenting out this line and __init__ method will never be invoked.

        # Usecase
        # 1. Implementing the Singleton pattern.
        # 2. Customizing object creation

        print("instance", instance)
        return instance

    def __init__(self, value):
        # Initialization after instance creation
        print("inside init")
        self.value = value
        print(value)

    def __call__(self, multiply) -> Any:
        return self.value * multiply
    
        # call can be called as a function i.e
        # obj=MyClass
        # result=obj(5) this will be like calling normal function.


obj = MyClass(10)
print(obj(5))
