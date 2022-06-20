
filename = "actions.txt"

f = open(filename);

cmd = f.readline();

requests = []

g = dict();

while (cmd != ""):
	cmd = cmd.strip();
	
	if (cmd[0 : 4] == "edge"):         ## add edge to graph g
		u, v, wt = cmd.split(" ")[1:];

		if (u in g):
			g[u][v] = wt;
		else:
			g[u] = {v : wt, };

		if (v in g):
			g[v][u] = wt;
		else:
			g[v] = {u : wt, };


	else:
		requests.append(cmd);

	cmd = f.readline();

f.close();

## now our graph is ready

print(g);

print("left cmd =", requests);
