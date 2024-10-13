import gc 
import time

gc.set_debug(False)
gc.set_threshold(300000,500,500)
#if we increase the threshold the code will speedup bcz gc will run less often and this will lead to more CPU memory,
#CPU memory will be increased but the speed of code also increases

class Link:
    def __init__(self,value,next) -> None:
        self.value=value
        self.next=next

    def __repr__(self) -> str:
        return self.value
    
main_link=Link(10,None)
my_list=[]
start=time.perf_counter()
for i in range(1,5000000):
    l=Link(i,main_link)
    my_list.append(l)
end=time.perf_counter()
print("time taken --- ",end-start)