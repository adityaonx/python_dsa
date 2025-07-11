class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        root=self.root
        if root is None:
            self.root=new_node
            return True
        
        while root:
            if value<root.value:    
                if root.left is None:
                    root.left=new_node
                    return True
                else:
                    root=root.left
            else:
                if root.right is None:
                    root.right=new_node
                    return True
                else:
                    root=root.right
                
bst=BST()
bst.insert(27)         
bst.insert(15)         
bst.insert(29)
bst.insert(26)
bst.insert(25)  
bst.insert(14)

def print_bst(root,x=0):
    if x==0:
        print(root.value)
    if root.left:
        print(root.left.value)
    if root.right:
        print(root.right.value)
    if not root.left or not root.right:
        return None
    print_bst(root.left,x=1)
    print_bst(root.right,x=1)
        
        
        
    

print_bst(bst.root)

        
    