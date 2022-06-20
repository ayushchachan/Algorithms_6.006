class Linked_List_Node:
	def __init__(self, x):
		self.item = x;
		self.next = None;

	def __str__(self):
		return str(self.item);

	def later_node(self, i):
		if (i == 0):
			return self;
		assert self.next;
		return self.next.later_node(i - 1);

class Linked_List_Seq:
	def __init__(self):
		self.head = None;
		self.size = 0;

	def __len__(self):
		return self.size;

	def __str__(self):
		return "(" + ")->(".join([str(x) for x in self]) + ")";

	def __iter__(self):
		current = self.head;
		while current:
			yield current.item;
			current = current.next;

	def build(self, X):
		for a in reversed(X):
			self.insert_first(a);

	def get_at(self, i):
		answer = self.head.later_node(i);
		return answer.item;

	def set_at(self, i, x):
		current = self.head.later_node(i);
		current.item = x;

	def insert_first(self, x):
		newest = Linked_List_Node(x);
		newest.next = self.head;
		self.head = newest;
		self.size = self.size + 1;

	def delete_first(self):
		if self.size > 0:
			x = self.head.item;
			self.head = self.head.next;
			self.size = self.size - 1;
			return x;

	def insert_at(self, i, x):
		if i == 0:
			self.insert_first(x);
			return;

		prev = self.head.later_node(i - 1);
		newest = Linked_List_Node(x);
		newest.next = prev.next;
		prev.next = newest;
		self.size = self.size + 1;

	def delete_at(self, i):
		if i == 0:
			self.delete_first();

		prev = self.head.later_node(i - 1);
		node = prev.next;

		prev.next = node.next;
		node.next = None;
		self.size = self.size - 1;
		return node.item;

	def insert_last(self, x):
		self.insert_at(self.size, x);

	def delete_last(self):
		self.delete_at(self.size - 1);


# l = Linked_List_Seq();
# l.insert_first(2);
# l.insert_first(3);
# l.insert_last(1);
# print("l =", l);
