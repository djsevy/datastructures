# Linked Lists

## Introduction
The last data structure we will be looking at are Binary trees! This will take from everything that we have gone over previously and it will use a few other concepts as well such as recursion. 

A binary tree is a data structure that organizes information using nodes. It is comprised of a root node and has no more than two nodes connected to other nodes. A node that has other nodes connected to it is a parent, and the nodes connected to the parent node are child nodes. 

In a binary search tree, nodes are organized by values that are lees than or greater than. Say that the tree beginning with the number 25 and you inserted a node with a value of 17 to the tree. That Node would be placed to the left of the 25. Again you add a node, this time with a value of 36. This node would  be placed to the right of the 25. Here is a picture to help illustrate this concept. In summary, smaller values will be placed to the left and larger values will be placed to the right.



## Example
In this example I'll show you how to create a Binary Search Tree, insert nodes into the tree, and how to traverse the tree forwards and backwards. In this example we will be using a few built in python methods and conditions. We will be using Yield, which allows us to create a generator that will return to us a value but not stop the loop completely. We will also be using __reversed__: this will initialize our going backwards method that that we will be able to iterate it backwards. 

```python
class BST:
    

    class Node:
        

        def __init__(self, data):
    
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        
        self.root = None

    def insert(self, data):
        
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  


    def _insert(self, data, node):
             
        if data < node.data:
         
            if node.left is None:
                
                node.left = BST.Node(data)
            else:
                
                self._insert(data, node.left)
        elif data > node.data:
      
                if node.right is None:
               
                    node.right = BST.Node(data)
                else:
                
                    self._insert(data, node.right)
        elif data == node.data:
            return None
    
  
    def __iter__(self):
      
        yield from self._traverse_forward(self.root)  
        
    def _traverse_forward(self, node):
       
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        yield from self.going_backwards(self.root)
            

    def going_backwards(self, node):
        if node is not None:
            yield from self._traverse_forward(node.right)
            yield node.data
            yield from self._traverse_forward(node.left)

  
tree = BST()
tree.insert(10)
tree.insert(6)
tree.insert(4)
tree.insert(12)
tree.insert(8)
tree.insert(7)
tree.insert(9)

print()
print('Traversing a BST forward')
for x in tree:
    print(x)


print()
print("Traversing a BST backwards")

for x in reversed(tree):
    print(x)
    
```

## Challenge

Now it's your turn! Using the same code, write a method that will return a true or false value as to whether or not our BST contains that requested value value. In other words, ask our program if it contains the value of 102 and if it does, have it return TRUE. if it doesn't have it return FALSE. Feel free to choose any number you'd like. Like always there will be a link that leads you to the solution.

- [Click here to view the solution](trees_challenge.py)