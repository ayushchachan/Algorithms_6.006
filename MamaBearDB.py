# At any point during her shopping, she would like to know the best bowls she’s seen
# so far: specifically, k bowls that are neither the ceiling(n−k/2) largest nor 
# the floor(n−k/2) smallest of the n bowls she has seen so far (or all n bowls when n ≤ k).
# 
# In this problem, you will design a database to
# help Mama Bear shop, supporting the following two operations:

# • record bowl(s): add a bowl of size s to the database
# • best bowls(): return the sizes of the k best bowls in the database

class MamaBearDB:
    def __init__(self, k):
        "Initialize database"
        self.k = k;
        self.smaller = [];       # a max heap 
        self.best = [];
        self.larger = [];        # a min heap, or use max heap by storing negative of values

    def record_bowl(self, s):
        "Add bowl with size s"
        if (len(self.best) < self.k):
            sorted_insert(self.best, s);

        else:
            if (s > self.best[len(self.best) - 1]):
                heap_insert(self.larger, -s);
                s = extract_max(self.larger) * -1
            elif (s < self.best[0]):
                heap_insert(self.smaller, s);
                s = extract_max(self.smaller);

            ## now s needs to be inserted in our best k elements
            sorted_insert(self.best, s);

            ## now we have k + 1 elements in self.best
            if (len(self.smaller) == len(self.larger)):
                heap_insert(self.larger, -1 * self.best.pop());
            
            else:
                heap_insert(self.smaller, self.best.pop(0));


    def best_bowls(self):
        "Return tuple of best bowls in sorted order"
        return tuple(self.best);

def sorted_insert(A, x):
    '''inserts x in sorted list A at appropriate location'''
    i = 0;
    while i < len(A):
        if (A[i] >= x):
            break;
        i = i + 1;
    A.insert(i, x);

## operations for max heap
def heapify_up(A, i = None):

    if i == None:
        i = len(A) - 1;
    while (i > 0 and A[parent(i)] < A[i]):
        A[parent(i)], A[i] = A[i], A[parent(i)];
        i = parent(i);

def heapify_down(A, i):
    l = left(i);
    r = right(i);

    largest = i;
    if (l < len(A) and A[l] > A[i]):
        largest = l;
    if (r < len(A) and A[r] > A[largest]):
        largest = r;

    if largest != i:
        A[i], A[largest] = A[largest], A[i];
        heapify_down(A, largest);

def extract_max(A):
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0];

    answer = A.pop();
    if A:
        heapify_down(A, 0);

    return answer;

def heap_insert(A, x):
    A.append(x);
    heapify_up(A);

def parent(i):
    return (i - 1) // 2;

def left(i):
    return 2*i + 1;

def right(i):
    return 2*i + 2;
