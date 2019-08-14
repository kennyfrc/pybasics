class QueueNode(object):

	def __init__(self, val, nxt, prev):
		self.value = val
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return f"[{self.value}:next={repr(nval)}:prev={repr(pval)}]"


class Queue(object):

	def __init__(self):
		self.tail = None
		self.head = None

	def shift(self,obj):
		"""pushes an object to the tail"""
		node = QueueNode(obj, None, None)
		if self.tail == None:
			self.tail = self.head = node
		else:
			next_val = self.tail
			next_val.prev = node
			self.tail = node
			self.tail.next = next_val
		print(f"self.head:{self.head}")
		print(f"self.head:{self.head.prev}")

	def unshift(self):
		"""removes the head"""
		if self.head == None:
			return None
		elif self.head == self.tail:
			unshifted_node = self.head
			self.head = self.tail = None
		else:
			unshifted_node = self.head
			self.head = self.head.prev
			self.head.next = None
		return unshifted_node.value

	def first(self):
		"""returns a reference to the first head element"""
		if self.head == None:
			return None
		return self.head.value


	def count(self):
		"""dfddf"""
		count = 0
		current_node = self.tail
		while current_node:
			current_node = current_node.next
			count += 1
		return count


	def drop(self):
		"""removes the head"""
		self.unshift()

