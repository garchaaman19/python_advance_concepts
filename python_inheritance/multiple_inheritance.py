class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        print("Hello from class B")
        super().greet()  #If this is removed then call to C wont happen as super() is critical for ensuring that all classes in the MRO participate in the method chain. 

class C(A):
    def greet(self):
        print("Hello from class C")
        super().greet()  # Calls greet from class B, then class A

class D(B,C):
    def greet(self):
        print("Hello from class D")
        super().greet()  # Calls greet from class B, then class A

# Example Usage
d = D()
d.greet()
print(D.mro())


#super 

#super() is critical for ensuring that all classes in the MRO participate in the method chain.
#super takes to next thing after current class in the MRO i.e next in line

#It’s not just about accessing the immediate parent; it’s about handling complex inheritance scenarios predictably.

#Without super(), you lose cooperative multiple inheritance, and the method chain can break.

#When super() is removed in B, Python doesn’t know to continue down the MRO chain. 
# It does not backtrack to C because that’s not how linear MRO works. 
# Python expects each class to decide whether to continue the chain by using super().