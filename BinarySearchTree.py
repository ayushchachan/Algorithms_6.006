
class BinaryNode:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None
        
    def subtree_iter(self):
        if self.left:
            yield from self.left.subtree_iter()
        yield self.item
        if self.right:
            yield from self.right.subtree_iter()
    
    def subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        else:
            return self
        
    def subtree_last(self):
        if self.right:
            return self.right.subtree_last()
        else:
            return self
        
    def successor(self):
        if self.right:
            return self.right.subtree_first()
        x = self
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y
    
    def predecessor(self):
        if self.left:
            return self.left.subtree_last()
        x = self
        y = x.parent
        while y and x == y.left:
            x = y
            y = y.parent
        return y

    def subtree_insert_before(self, newNode):
        if self.left:
            x = self.left.subtree_last()
            x.right, newNode.parent = newNode, x
        else:
            self.left, newNode.parent = newNode, self
            
    def subtree_insert_after(self, newNode):
        if self.right:
            x = self.right.subtree_first()
            x.left, newNode.parent = newNode, x
        else:
            self.right, newNode.parent = newNode, self
    
    def subtree_delete(self):
        pass
            