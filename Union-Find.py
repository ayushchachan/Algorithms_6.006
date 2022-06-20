
class QuickUnionUF:
	def __init__(self, n):
		self.id = [i for i in range(n)];
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

		if (proot != qroot):
			self.id[proot] = qroot;
			self.numComponents -= 1;

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



filename = "test/largeUF.txt"

fileReader = open(filename)
V = int(fileReader.readline());

uf1 = WeightedQuickUnionUF(V);

nextLine = fileReader.readline();

while (nextLine != ""):
	u, v = nextLine.split(" ");
	u, v = int(u), int(v);
	uf1.union(u, v);
	nextLine = fileReader.readline();

print(uf1.count())

fileReader.close();