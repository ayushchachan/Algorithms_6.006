## format of input file
## {no. of vertex} {no of edges}
## {vertex u} {vertex v} {weight}
## --  -  -  -  -  -  -  -  - -  - 

## --  -  -  -  -  -  -  -  - -  - 
## {vertex u} {vertex v} {weight}

class WeightedQuickUnionUF:
    def __init__(self, n):
        self.id = [i for i in range(n)];
        self.sz = [1 for i in range(n)];
        self.numComponents = n;

    def count(self):
        '''returns the number of connected components'''
        return self.numComponents;

    def connected(self, p, q):
        '''returns true if pa nd q are in same component, i.e. p and q are connected'''
        return self.find(p) == self.find(q);

    def find(self, p):
        assert p >= 0;
        assert p < len(self.id);

        while self.id[p] != p:
            p = self.id[p];
        return p;

        

    def union(self, p, q):
        assert (p >= 0 and q >= 0);
        assert (p < len(self.id) and q < len(self.id));

        proot = self.find(p);
        qroot = self.find(q);

        if (proot == qroot):    return;

        if (self.sz[proot] > self.sz[qroot]):
            self.id[qroot] = proot;
            self.sz[proot] += self.sz[qroot];
        else:
            self.id[proot] = qroot;
            self.sz[qroot] += self.sz[proot];

        self.numComponents -= 1;

def construct_graph(filename):

    fileReader = open(filename)

    V, E = fileReader.readline().split(" ");

    V, E = int(V), int(E)

    edges = [];

    Adj = {}

    l = fileReader.readline()

    while (l != ""):
        u, v, wt = l.split(" ")
        # print("u =", u, ", wt =", wt)
        u, v, wt = int(u), int(v), int(wt);

        if (u in Adj):
            Adj[u][v] = wt;
        else:
            Adj[u] = {v : wt}

        if (v in Adj):
            Adj[v][u] = wt;
        else:
            Adj[v] = {u : wt};
        
        edges.append((u, v, wt));
        l = fileReader.readline()
    return Adj, edges;


addrss = "test/edges.txt"
g1, all_edges = construct_graph(addrss);
print(len(g1), "vertices");

V = len(g1);

count = 0;

for k in g1:
    count += len(g1[k]);
print(count//2, " edges")

print("len(all_edges) =", len(all_edges));


def weight(e):
    '''returns the weight of an edge; an edge is a tuple of form (u, v, wt)'''
    return e[2];

all_edges.sort(key = weight, reverse = True);

# performing kruskal's algorithm
A = set();

uf1 = WeightedQuickUnionUF(V);

while (all_edges and len(A) != V - 1):
    u, v, wt = all_edges.pop();

    ## if adding above egde to A forms a cycle then skip this edge
    ## else add above edge to A

    if not uf1.connected(u - 1, v - 1):
        
        uf1.union(u - 1, v - 1);
        A.add((u, v, wt));

if len(A) != V - 1:
    print("MST cannot be constructed since graph is not connected.")
else:

    minwt = 0;
    for e in A:
        minwt += e[2];

    print("weight of minimum spanning tree = " , minwt);


