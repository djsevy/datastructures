# Linked Lists

## Introduction
Linked lists are a incredibly interesting data structure and a great concept to learn before learning about trees. A linked list is exactly as it sounds. It is a list of nodes that are linked by what is called a pointer and rather than being sequential, this pointer will connect to node's location in memory. 

To construct a linked list, you create the "head"  and the "tail" of the list. The "head" is the first node in the linked list and the tail is the last node. The "head" node will point to whatever node is next in the list and the tail points to nothing. 

In order to construct a linked list you need to implement two classes, LinkedList and Node. This will enable you to create an object.

Working with Linked lists is nice as it proves a relatively seamless way to navigate through each node as well as removing them.

## Common Implementations
- prepend()
- append()
- remove_head()
- remove_tail()
- remove(value)
- size()
- empty()

## Big O Notation

When it comes to Big O, if we are simply adding nodes onto the end of the list by means of the tail, we are using O(1). On the opposite side of that, if we are going to remove a node from the tail we actually need to iterate through the entire list to set the new pointer for the new tail. Because we are iterating through the entire list we are using O(n). 

When it comes to adding an item by means of the head node, it is essentially the same process as adding a node via the tail, thus it is O(1). If we a removing an node from the head, all we are doing using head.next(). This sets the new nodes position and allows us to remove the previous node. This is also O(1).

## Example

For this example I'll show you how to construct your linked list, add an item to the list, and then print that list.

```python
class Node:

    # This class will be called anytime a new node is created.
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
   
   
    # this will initialize the linked list.
    # It will also create a new node.
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_ll(self, value):
        front = self.head
        while front is not None:
            print(front.value)
            front = front.next


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
```


## Challenge