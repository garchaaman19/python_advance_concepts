class CustomTuple(tuple):
    def __new__(cls, iterable):
        # Filter only even numbers before creating the tuple
        even_numbers = [x for x in iterable if x % 2 == 0]
        # Call the parent __new__ to create the tuple
        instance = super().__new__(cls, even_numbers)
        #NOTE here new method of super class i.e tuple accepts argument thats why we can pass argument apart from cls.

        return instance
    
    # def __init__(self,iterable) -> None:
    #     print("init was called")

custom = CustomTuple((1, 2, 3, 4, 5, 6))
print(custom)  # Output: (2, 4, 6)

#The below code will throw an error as we try to pass an argument bcz the class inherits from 
#object class and new method in that class does not accept any arguments
# class Custom():
#     def __new__(cls,iterable):
#         instance=super().__new__(cls,iterable)
#         return instance
    

# obj=Custom(1)
# print(obj)