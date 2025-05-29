class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self,value):
        new_node=Node(value)
        self.root=new_node
    def insert(self,value):
        new_node=Node(value)
        if self.root is None: 
            self.root=new_node
            return True
        tmp=self.root
        while True:
            if tmp.value==value: 
                return False
            if value < tmp.value:
                if tmp.left is None:
                    tmp.left=new_node
                    return True
                tmp=tmp.left  
            else:
                if tmp.right is None:
                    tmp.right=new_node
                    return True
                tmp=tmp.right
            
    # def print(self):
    #     pre=self.root
    #     tmp=self.root
    #     level=0
    #     while True:
    #         print("level",level)
    #         print("root",tmp.value)
    #         if tmp.left:
    #             print("left",tmp.left.value)
    #         elif tmp.left is None:
    #             print("left","None")
    #         if tmp.right:
    #             print("right",tmp.right.value)
    #         elif tmp.right is None:
    #             print("right","None")
    #         level+=1
    #         if tmp.left:
    #             tmp=tmp.left
    #         elif tmp.right:
    #             tmp=tmp.right
    #         else:
    #             return False
    def contains(self,value):
        tmp=self.root
        while True:
            if tmp.value==value:
                return True
            else:
                if tmp.left:
                    if tmp.left==value:
                        return True
                    else:
                        tmp=tmp.left
                elif tmp.right:
                    if tmp.right==value:
                        return True
                    else:
                        tmp=tmp.right
                else:
                    return False
            
myBST=BST(100)
myBST.insert(40)
myBST.insert(110)
myBST.insert(150)
myBST.insert(105)
myBST.insert(30)
myBST.insert(50)
a=myBST.contains(50)
print(a)