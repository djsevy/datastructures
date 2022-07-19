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


    def print_ll(self):
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

    # Prepend will create a node and 
    # add it to the beinning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

ll = LinkedList(1)
ll.append(2)
ll.append(7)
ll.append(31)
ll.append(24)
ll.append(8)
ll.append(1)
ll.print_ll()
    
```
- [Click here to return the the previous page](linkedlists.md)

- [Click here to return to the first page](README.md)
