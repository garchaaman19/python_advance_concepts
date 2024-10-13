# class SimpleProxy:
#         # def __init__(self,cls,obj) -> None:
#         #     self.obj=obj
#         #     self.cls=cls
#         # def __getattr__(self,item):
#         #     attr=getattr(self.cls,item)
#         #     if hasattr(type(attr),'__get__'):
#         #         attr=attr.__get__(self.obj)
#         #     return attr

#         def __init__(self,obj) -> None:
#             self.obj=obj


#         def __getattr__(self,item):
#             print("self.obj,item",self.obj,item)
#             return getattr(self.obj,item)

# # class A:
# #         def f(self):
# #             print("inside A")

# # class B:
# #         def f(self):
# #             print("B")
# #             KindaSuperProxyObject(A,self).f()


# obj=[1,2,3]
# proxy=SimpleProxy(obj)
# proxy.append(4)
# print(obj)
# print(proxy)
class X:
    def __init__(self, value):
        print("Initializing class X")
        self.value = value
        print("value in x", self.value)
        super().__init__(value)


class Y:
    def __init__(self, value):
        print("Initializing class Y")
        self.value = value
        print("value in Y", self.value)
        super().__init__()


class Z(X, Y):
    def __init__(self, value):
        print("Initializing class Z")
        super().__init__(value)
        self.value = value
        print("Value in Z", self.value)


obj = Z(10)
