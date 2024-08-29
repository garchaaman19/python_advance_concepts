class MyClass:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MyClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
                print("Initializing instance")
                # self.value = value
                self.abc = True
                print(dir(self))

# Creating an instance of MyClass
obj = MyClass()
obj1=MyClass()
# obj2=MyClass(30)

print(f"Value: {obj}")
# print(f"Value: {obj1.value}")
# print(f"Value: {obj2.value}")
