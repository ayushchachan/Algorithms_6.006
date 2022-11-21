
from importlib.machinery import SourcelessFileLoader
from turtle import right


class BST_Node:
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



class BinaryTree:
    def __init__(self, Node_Type = BST_Node):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type           
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        for node in self.root.subtree_iter():
            yield node.item
            
    def build(self, X):
        A = [z for z in X]
    
        def build_subtree(A, i, j):
            if i < j:
                mid = (i + j) // 2
                root = BST_Node(A[mid])
                root.left = build_subtree(A, i, mid)
                root.right = build_subtree(A, mid + 1, j)
                return root
            else:
                return None
        
        self.root = build_subtree(A, 0, len(A))
        self.size = len(A)
        

            

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.item)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) +
                right_line
                for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

import random;

Z = [random.randint(1, 200) for i in range(20)];


print(Z);

tree1 = BinaryTree();
tree1.build(Z);

print(tree1);

