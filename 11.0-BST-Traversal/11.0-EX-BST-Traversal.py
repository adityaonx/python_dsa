class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
 

    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False      
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

 
          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 
        
    def delete_node(self,value):
        self.__delete(self.root,value)
    
    def __delete(self,curr_node,value):
        if curr_node.value==None:
            return None
        if value<curr_node.value:
                curr_node.left= self.__delete(curr_node.left,value)
        elif value>curr_node.value:
                curr_node.right= self.__delete(curr_node.right,value)
        return curr_node

    def BFS(self):
        current_node=self.root
        queue=[]
        results=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results=[]
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
                
bfs=BinarySearchTree()
bfs.insert(47)
bfs.insert(21)
bfs.insert(76)
bfs.insert(18)
bfs.insert(27)
bfs.insert(52)
bfs.insert(82)

print(bfs.dfs_pre_order())


        
