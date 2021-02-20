class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # INSERTS NEW NODE VALUE TO BSTNODE
    def insert(self, value):
        if self.value == None:
            self.value = BSTNode(value)

        # less than (to the left)
        elif value < self.value:
            if self.left == None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)
        # greater than (to the right)
        else:
            if self.right == None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    # CHECKS TO SEE IF THERES ALREADY A SPECIFIC NODE IN BSTNODE
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
               return self.left.contains(target) 
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
