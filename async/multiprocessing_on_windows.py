from multiprocessing import Process
import time
"""
Understanding Multiprocessing Behavior on Windows

Context:
When using the multiprocessing module on Windows, it's crucial to be aware of how child processes are spawned and how the main process behaves during their execution.

Behavior Description:

Concurrent Execution:

When a new process is spawned using Process(target=worker), the child process starts executing the script from the top independently of the main process.
The main process does not automatically wait for the child process to complete before proceeding.
Immediate p.join():

Placing p.join() immediately after p.start() does not block the main process, allowing it to proceed independently while the child process is still running.
Potential for Unexpected Behavior:

If the main process relies on the results or side effects of the child process, it may proceed independently, leading to race conditions and unexpected behavior.
For example, variables modified in the child process might not be in the state expected by the main process.
Guidance:

The main process should wait for the child process to complete before continuing, especially when dependencies exist between them.

Solution

The p.join() method must be placed after the main process's code, ensuring it waits for the child process to complete before proceeding.


p = Process(target=worker)
p.start()

while counter < 6:
    print(f"Main process: {counter}")
    counter += 1
    time.sleep(1)

p.join()  # Now, wait for the worker process to complete


"""

print("I am at top")
counter = 0

def worker():
    print("inside worker")
    global counter
    print("counter value in worker",counter)
    while counter < 5:
        print(f"Worker process: {counter}")
        counter += 1
        time.sleep(1)

# Without if __name__ == '__main__':
# The following code will be executed in each spawned process


# Main process continues running
# counter

if __name__=="__main__":
    # worker()
    # Creating a new process
    p = Process(target=worker)
    p.start()
    #NOTE 
    #above wont get executed immediately,.join() wont block on windows. 
    #on Windows, the main process does not wait for the child processes to complete automatically when using the start() method. The join() method must be explicitly called to wait for the child process to finish.
    p.join()    

#the below will be executed immeidately after creating process and after completion caller will go back to process 
while counter < 6:
    print(f"Main process: {counter}")
    counter += 1
    time.sleep(1)

print("I am out of main")
print("counter value",counter)

