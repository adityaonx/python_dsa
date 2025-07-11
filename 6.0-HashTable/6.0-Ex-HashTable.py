class HashTable:
    def __init__(self,size=7):
        self.dataMap=[None]*size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*29)%len(self.dataMap)
        return my_hash
    def print_table(self):
        for i,val in enumerate(self.dataMap):
            print(i,":",val) 
    
    def set_item(self,key,value):
        index=self.__hash(key)
        if self.dataMap[index] is None:
            self.dataMap[index]=[]
        self.dataMap[index].append([key,value])
        #[None,None,[[key,value]],None]
    def get_item(self,key):
        index=self.__hash(key)
        if len(self.dataMap[index])!=0:
            add_list=self.dataMap[index]
        for add in add_list:
            if add[0]==key:
                return add[1]            
    def keys(self):
        key_list=[]
        data_list=self.dataMap #[[],[],None]
        for add in data_list:
            if add is not None:
                for items in add:
                    key_list.append(items[0])
        return key_list
h=HashTable()
h.set_item("name","aditya")
h.set_item("roll",101)
h.set_item("id",1)
h.set_item("age",28)
# h.print_table()
# print("get_item",h.get_item("age"))
print(h.keys())
