def reorder_students(L):
    '''
    Input:  L    | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''
    ##################
    # YOUR CODE HERE #
    ##################

    n = len(L) // 2;

    node = L.head;
    for i in range(n - 1):
        node = node.next;

    print("list = ", L);
    a = node;
    b = node.next;
    
    print("a =", a);
    print("b =", b);

    prev = node;
    
    node = node.next;
    
    for i in range(n):
        # print("node =", node)
        c = node.next;
        node.next = prev;
        prev = node;
        node = c;

    c = prev;
    a.next = c;
    b.next = None;


    return

from Linked_List_Seq import Linked_List_Seq;

l = Linked_List_Seq();

for i in range(1, 10):
    l.insert_first(i);

for i in range(11, 20):
    l.insert_last(i);

print("l =", l);
print("--------------")
reorder_students(l)
print("l =", l);
