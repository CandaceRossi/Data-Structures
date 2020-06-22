"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        #add an element to front of our array
        self.storage.insert(0, value)
        print(value)

    def pop(self):
        if len(self.storage) == 0: #check if empty
            return None
        #remove the first element in storage
        self.size -= 1
        node = self.storage.pop(0)
        return node

  

# class Stack:
#     def __init__(self):
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.storage.len()

#     def push(self, data):
#         newNode = Node(data)
#         newNode.next = self.root
#         self.root = newNode
#         print "% d pushed to stack" % (data)

#     def pop(self):
#         if (self.isEmpty()):
#             return float("-inf")
#         temp = self.root
#         self.root = self.root.next
#         popped = temp.data
#         return popped
