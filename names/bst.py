class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # max value is on the right
        # move right until you can't move
        # if you can't move you are on the max value
        if self.right is None:
            # Base Case
            # You can't go right therefore you are at the max value
            # return max value
            return self.value
        else:
            # Recursive Case
            # Go right and move closer to the base case
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, cb):
        # This is a recursive DFT
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # print("node", self.value)
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()






