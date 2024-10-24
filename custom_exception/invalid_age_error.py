# Creating a custom exception by inheriting from Exception class
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 65."):
        self.age = age
        self.message = message
        super().__init__(self.message)
        #if we comment out super method there wont be any change in output unless __str__ method is also commented 
        #As  __str__ method is called below it will ensure that the attributes message,age are printed correctly. 

   
    #below will format the string message for us, if we comment it out The message from super().__init__(self.message) is used as the string representation of the exception.
    #Any custom attributes (like self.age) will not be part of the output because the default __str__ implementation doesn't know how to include them.
    #The print function calls __str__() on the exception object. 
    def __str__(self):
        return f'{self.age} -> {self.message}'

def check_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError(age)
    else:
        print("Age is valid.")

# Test cases
try:
    check_age(15)  # This will raise the custom InvalidAgeError
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    check_age(30)  # This will print "Age is valid."
except InvalidAgeError as e:
    print(f"Error: {e}")
