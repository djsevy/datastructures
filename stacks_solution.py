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
