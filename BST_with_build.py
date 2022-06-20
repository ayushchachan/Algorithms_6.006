class Binary_Node:
    ''' '''
    def __init__(self, x):
        self.key = x;
        self.parent = None;

        self.left = None;
        self.right = None;


    # navigatory operatons
    def subtree_iter(self):
        if (self.left):
            yield from self.left.subtree_iter();
        yield self;
        if (self.right):
            yield from self.right.subtree_iter();
            
    
    def subtree_first(self):
        if (self.left):
            return self.left.subtree_first();
        else:
            return self;


    def subtree_last(self):
        if (self.right):
            return self.right.subtree_last();
        else:
            return self;


    def successor(self):
        if (self.right):
            return self.right.subtree_first();

        x = self;
        p = x.parent;

        while (p and x == p.right):
            x = p;
            p = x.parent;
        return p;


    def predecessor(self):
        if (self.left):
            return self.left.subtree_last();

        x = self;
        p = x.parent;

        while (p and x ==  p.left):
            x = p;
            p = x.parent;
        return p;


    # dynamic operations
    def subtree_insert_before(self, B):
        '''
        Inserts a node <B> before node <self> in
        traversal order.
        '''
        if (self.left is None):
            self.left = B;
            B.parent = self;
        else:
            z = self.left.subtree_last();
            z.right = B;
            B.parent = z;


    def subtree_insert_after(self, B):
        '''
        Inserts a node <B> after node <self> in
        traversal order.
        '''
        if (self.right is None):
            self.right = B;
            B.parent = self;
        else:
            z = self.right.subtree_first();
            z.left = B;
            B.parent = z;


    def subtree_delete(self):
        '''Delete the node <self> from the tree, maintaining
        the traversal order.
        '''
        if (self.left or self.right):
            if (self.left):
                z = self.left.subtree_last();
            else:
                z = self.right.subtree_first();

            self.key, z.key = z.key, self.key;
            return z.subtree_delete();
        else:
            if (self.parent):
                if (self.parent.left == self):
                    self.parent.left = None;
                else:
                    self.parent.right = None;
                self.parent = None;
            return self;

# Top-Level Data Structure

class Binary_Tree:
    def __init__(self, Node_Type = Binary_Node):
        self.root = None;
        self.size = 0;
        self.Node_Type = Node_Type;

    def __len__(self):
        return self.size;

    def __iter__(self):
        if (self.root):
            yield from self.root.subtree_iter();

    def build(self, A):
        X = [a for a in A];

        def build_subtree(X, i, j):
            if (i > j):
                return None;

            c = (i + j)//2;

            subtree_root = Binary_Node(X[c]);

            subtree_root.left = build_subtree(X, i, c - 1);
            subtree_root.right = build_subtree(X, c + 1, j);

            return subtree_root;


        self.root = build_subtree(X, 0, len(X) - 1);
        self.size = len(X);


    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
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

tree1 = Binary_Tree();
tree1.build(Z);

print(tree1);