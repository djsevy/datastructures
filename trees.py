# Example and Solution

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
      
        yield from self._traverse_forward(self.root)  # Start at the root
        
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


    def contains(self, data):
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else: 
                return True
        return False
  
tree = BST()
tree.insert(10)
tree.insert(6)
tree.insert(4)
tree.insert(12)
tree.insert(8)
tree.insert(7)
tree.insert(9)


print('\ntraversing a BST forward')
for x in tree:
    print(x)

print("\nTraversing a BST backwards")

for x in reversed(tree):
    print(x)

print()
print('Using our contains method')
print(7 in tree)
print(19 in tree)
print(655 in tree)
print(9 in tree)
print(4 in tree)




        