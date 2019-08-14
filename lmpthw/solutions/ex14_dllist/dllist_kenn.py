class DoubleLinkedListNode(object):
	def __init__(self, value, nxt, prev):
		self.value = value
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

	def __init__(self):
		self.begin = None
		self.end = None

	def _invariant(self):
		"""None yet"""
		if self.begin == None:
			assert self.begin == self.end == None
		elif self.count() == 1:
			assert self.begin == self.end
		elif self.begin == self.end:
			assert self.begin.prev == None
			assert self.end.next == None

	def push(self, obj):
		"""Appends a new value on the end of the list."""
		node = DoubleLinkedListNode(obj, None, None)
		if self.begin == None:
			self.begin = self.end = node
		else:
			node.prev = self.end
			node.prev.next = self.end = node
			assert self.end.prev != self.end

	def pop(self):
		"""Removes the last item and returns it.""" 
		if self.end == self.begin == None:
			return None
		elif self.begin == self.end:
			popped_node = self.end
			self.begin = self.end = None
			return popped_node.value
		else:
			popped_node = self.end
			self.end = self.end.prev
			self.end.next = None
			return popped_node.value

	def shift(self, obj):
		 """Actually just another name for push, but to the front"""
		 node = DoubleLinkedListNode(obj, None, None)
		 if self.begin == self.end == None:
		 	self.begin = self.end = node
		 else:
		 	next_node = self.begin
		 	self.begin = next_node.prev = node
		 	self.begin.next = next_node

	def unshift(self):
		"""Removes the first item (from begin) and returns it."""
		if self.end == self.begin == None:
			return None
		elif self.begin == self.end:
			unshifted_node = self.begin
			self.begin = self.end = None
			return unshifted_node.value
		else:
			unshifted_node = self.begin
			self.begin = self.begin.next
			return unshifted_node.value

	def detach_node(self, node):
		if node == self.end:
			# only node or last node
			self.pop()
		elif node == self.begin:
			# first node
			self.unshift()
		else:
			# in the middle
			prev = node.prev
			nxt = node.next
			prev.next = nxt
			nxt.prev = prev


	def remove(self, obj):
		node = self.begin
		count = 0

		while node:
			if node.value == obj:
				self.detach_node(node)
				return count
			else:
				count += 1
				node = node.next

		return -1

	def first(self):
		"""Returns a *reference* to the first item, does not remove."""
		return self.begin.value

	def last(self):
		"""Returns a reference to the last item, does not remove."""
		return self.end.value

	def count(self):
		"""Counts the number of elements in the list."""
		count = 0
		current_node = self.begin
		while current_node:
			count += 1
			current_node = current_node.next
		return count


	def get(self, index):
		"""Get the value at index."""
		count = 0
		current_node = self.begin
		while count != index:
			count += 1
			current_node = current_node.next
		if current_node:
			return current_node.value
		else:
			return None

	def dump(self, mark):
		"""Debugging function that dumps the contents of the list."""