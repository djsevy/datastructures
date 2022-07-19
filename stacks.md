# Stacks

## Introduction

A stack is a dataset that operates based on the principal called LIFO(last in, first out). To help illustrate this, imagine a pile of clothes in a hamper that just come out of the dryer. As you begin to put away the clothes, you will be put away the last item that was placed in the hamper first. 

## Common operators when implementing stacks
- append()
- pop() 
- len() 


## Big O Notation
- When it comes to Big O Notation and stacks, it really depends on how you construct your stack. For example, if you construct a list and you want to add and Item to the end of the stack, that would be O(1), because no matter how many items you are adding, you won't be indexing all the items before the one your adding. Other the other end of the list, we would be looking at O(n). The reason we would use O(n) instead of O(1) is because we would have to index each item that comes before the one you're adding or removing. To illustrate this point imagine a printed essay that you are stacking as each page is printed. As a page comes out of the printer you put that page on the top of the stack, that is O(1). However if you make a change to just one of the pages, say page 7, and just print out that page so that you can replace it with the old page 7. You would have to pick up all of the pages that had been placed on the stack after 7, the take out page 7, the replace each page after 7 again. This is O(n)

## Why Are Stacks Useful?
- A real world example of stacks would be a web browser. Lets say you started on google first, then went to BYUI.edu, then, facebook, handshake, and last youtube. Right there is a stack, starting with google and ending with youtube. If you press the back button, you remove youtube from the stack and return to handshake. If you repeat this process you'll eventually end right back at google. 


## Example 
- For our example we will create a stack of numbers from 1-100. However, we will only add even numbers. Then we will remove 10 items form the list and we should return 78.

 ```python 
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

```

## Challenge
Now it's your turn! Create a stack of all the odd numbers that weren't included in out last problem. 

- [Click here to view the solution](stacks_solution.md)
- [Click here to return to the first page](README.md)



    
        
