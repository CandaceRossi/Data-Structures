"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Queue:
    def __init__(self, value):
    self.size = 0
    #add the first node to the queue
    self.storage = BSTNode(value)

    def __len__(self):
        return self.size

    def enqueue(self, value):
       #add the new value to the tail of our list
       self.size += 1
       self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        #remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()
        return value

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
    
        if value < self.value:
                # If self.left is already taken by a node
                # make that (left) node, call insert
                # set the left child to the new node with new value
            if self.left is None:
                self.left = BSTnode(value)
            else: 
                self.left.insert(value)

        if value >= self.value: 
               # If self.right is already taken by a node
               # make that (right) node call insert
               # set the right child to the new node with new value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)            

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value is more than target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value >= target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)
        
        return found


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()     

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call function on the current value fn(self.value)
       fn(self.value)
       #if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn) 
       #if you can go right, call for_each on the left tree
        if self.right:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        fn(self.node)
        if self.left:
            return self.left.for_each(fn)
        print self.node 


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue for nodes
        # Base Case
        if root is None:
            return
     # Create an empty queue for level order traversal
        queue = []
    # Enqueue Root and initialize height
        queue.append(node)
        #while queue is not empty
        while(len(queue) > 0):
            print(queue[0].value)
            #remove the first node from the queue
            node = queue.pop(0)
            #print the removed node
            #add all children into the queue
            #Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
         #create a stack for nodes
        #add the first node to the stack
        #while stack is not empty
            #remove the first node from the stack
            #print the removed node
            #add all children into the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
           #first print the data of Node
            print(node.value)
           #then recur on left child
            pre_order_dft(node.left)
           #recur on right child
            pre_order_dft(node.left)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            #first recur on left child
            post_order_dft(node.left)
            #print the data of node
            print(node.value)    

root_node = BSTNode(8)
root_node.insert(3)
root_node.insert(10)
root_node.insert(9)
root_node.insert(12)

print_node = lambda x: print(f'current_node is: {x}')

root_node.for_each(print_node)
