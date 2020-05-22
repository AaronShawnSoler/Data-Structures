import sys
sys.path.append('../binary_search_tree')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or right need to be valid nodes
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == None:
            return False
        if self.value == target:
            return True
        if self.value > target:
            if self.left != None:
                return self.left.contains(target)
        if self.right != None:
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right == None:
            return self.value

        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        bsfQueue = Queue()

        bsfQueue.enqueue(node)

        while bsfQueue.len() > 0:
            tNode = bsfQueue.dequeue()
            print(tNode)
            if tNode.left:
                bsfQueue.enqueue(tNode.left)
            if tNode.right:
                bsfQueue.enqueue(tNode.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if node.left:
            node.left.in_order_print(node.left)
        if node.right:
            node.right.in_order_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
