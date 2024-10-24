class MyItr:
    """
    Iterator to print numbers from 1 to 10 

    """
    def __init__(self,num) -> None:
        print("inside init")
        self.num=num

    # def __iter__(self):
    #     print("inside iter")
    #     return self
    
    def __next__(self):
        print("inside next")
        if self.num <=5:
            current=self.num
            self.num+=1
            return current
        else:
            raise StopIteration
        
numbers=MyItr(1)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

#if we need to use in below way then the MyItr class must implement __iter__ method. 


# itr=iter(numbers)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))