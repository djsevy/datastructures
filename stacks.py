# Example problem 

def even_stack():
        
        
    
    stack = []
    for i in range(100):
        if i != 0:
            if i % 2 == 0:
                stack.append(i)
    
    for i in range(10):
        stack.pop()
    return stack

print(even_stack())


# Challenge Solution

def final_stack():
        
        
    stack = []
    even_stack = []
    odd_stack = []
    for i in range(101):
        stack.append(i)
        if i != 0:
            if i % 2 == 0:
                even_stack.append(i)
            else:
                odd_stack.append()
    return odd_stack

print(final_stack())



