from dllist import DoubleLinkedList

def bubble_sort(numbers):
	"""Sorts a list of numbers using bubble sort."""
	while True:
	# start off assuming it's sorted
		is_sorted = True
		# comparing 2 at a time, skipping ahead
		node = numbers.begin.next
		while node:
		# loop through comparing node to the next
			if node.prev.value > node.value:
			# if the next is greater, then we need to swap
				node.prev.value, node.value = node.value, node.prev.value
			# oops, looks like we have to scan again
				is_sorted = False
			node = node.next
		if is_sorted: break

def merge_sort(numbers):
	if numbers.count() < 2:
		return numbers

	left, right = DoubleLinkedList(), DoubleLinkedList()

	node = numbers.begin
	length = numbers.count()
	count = 0
	
	while node:
		# print("node>>>>", node.value)
		if count < length // 2:
			# print("left>>>", left)
			left.shift(node.value)
		else:
			# print("right>>>", right)
			right.shift(node.value)
		count += 1
		node = node.next

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	result = DoubleLinkedList()

	# if left == None: return right
	# if right == None: return left

	while left.count() != 0 and right.count() != 0:
		if left.get(0) < right.get(0):
			# val = left.unshift()
			result.shift(left.unshift())
			# left.detach_node(left.begin)
			# print("left-count:", left.count())
		else:
			# val = right.unshift()
			result.shift(right.unshift())
			# right.detach_node(right.begin)
		# result.shift(val)
		# print(result.unshift())


	while left.count() != 0:
		# val = left.unshift()
		# result.shift(val)
		result.shift(left.unshift())
		# left.detach_node(left.begin)

	while right.count() != 0:
		# val = right.unshift()
		# result.shift(val)
		result.shift(right.unshift())
		# right.detach_node(right.begin)

	test = result.begin

	while test:
		print(test.value)
		test = test.next

	return result


