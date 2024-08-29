class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
singleton3 = Singleton()

print(singleton1 is singleton2)  # Output: True
print(singleton1 is singleton3)  # Output: True
print(singleton3 is singleton1)  # Output: True

print("------------------")
print(id(singleton1))
print(id(singleton2))
print(id(singleton3))

#SECOND EXAMPLE using decorators 

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Creating a database connection")

# Test the singleton behavior
db1 = DatabaseConnection()  # Output: Creating a database connection
db2 = DatabaseConnection()  # No output; the same instance is reused

print(db1 is db2)  # Output: True
