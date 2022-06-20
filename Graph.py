# a graph
#
addrss = input("Enter the filename: ")


def construct_graph(filename):

    fileReader = open(filename)

    V = int(fileReader.readline())
    E = int(fileReader.readline())

    Adj = {}

    l = fileReader.readline()

    while (l != ""):
        u, w = l.split(" ")
        # print("u =", u, ", w =", w)
        u = int(u)
        w = int(w)

        if (u in Adj):
            Adj[u].add(w)
        else:
            Adj[u] = {w}

        if (w in Adj):
            Adj[w].add(u)
        else:
            Adj[w] = {u};
               
        l = fileReader.readline()
    return Adj;

g1 = construct_graph(addrss);

print(len(g1), "vertices");

count = 0;

for k in g1:
    count += len(g1[k]);
print(count//2, " edges")


def bfs(Adj, s):
    parent = {s:None}
    level = [[s]];
    
    while level[-1]:
        nextLevel = [];

        for u in level[-1]:
            for v in Adj[u]:
                if v not in parent:
                    parent[v] = u;
                    nextLevel.append(v);
        level.append(nextLevel);
    return parent;

def cc(Adj):
    count = 0;

    parent = {};
    
    for u in Adj:
        if u not in parent:
            tree = bfs(Adj, u);
            count += 1;
            parent.update(tree);
    return count;


print(cc(g1), " connected components");

def dfs(Adj):
    parent = {};
    for u in Adj:
        if u not in parent:
            parent[u] = None;
            dfs_visit(Adj, u, parent);
    return parent;

def dfs_visit(Adj, s, parent):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s;
            dfs_visit(Adj, v, parent);


