class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.item);

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0;

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __len__(self):
        return self.size;

    def __str__(self):
        return "(" + ')-('.join([str(x) for x in self]) + ")"

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        newest = Doubly_Linked_List_Node(x)
        newest.next = self.head;
        
        self.head = newest;

        if (newest.next):
            newest.next.prev = newest;
        else:
            self.tail = newest;
        self.size += 1;
        print("list =", self);

    def insert_last(self, x):
        newest = Doubly_Linked_List_Node(x)
        newest.prev = self.tail;

        self.tail = newest;

        if (newest.prev):
            newest.prev.next = newest;
        else:
            self.head = newest;
        self.size += 1;
        print("list =", self);

    def delete_first(self):
        # print("list before delete first =", self);
        if (self.size > 0):
            x = self.head.item;
            a = self.head;
            self.head = self.head.next;

            a.next = None;
            if (self.head):
                self.head.prev = None;
            else:
                self.tail = None;
            self.size -= 1;
            # print("list after delete first =", self);
            print("list =", self);
            return x

    def delete_last(self):
        # print("list before delete last =", self);
        if (self.size > 0):
            x = self.tail.item;
            b = self.tail;
            self.tail = self.tail.prev;

            b.prev = None;
            if (self.tail):
                self.tail.next = None;
            else:
                self.head = None;
            self.size -= 1;
            # print("list after delete last =", self);
            print("list =", self);
            return x

    