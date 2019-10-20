from random import randint
from collections import deque
import pdb


def random_list(count):
    numbers = []
    for i in range(0, count):
        numbers.append(randint(0, 10000))
    return numbers

def merge_sort(numbers):
	if len(numbers) <= 1:
		return numbers

	left, right = [], []

	for idx, e in enumerate(numbers):
		if idx < len(numbers) // 2:
			left.append(e)
		else:
			right.append(e)

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)


def merge(left, right):
	result = []

	if left == None: return right
	if right == None: return left

	while left and right:
		if left[0] < right[0]:
			result.append(left[0])
			left.remove(left[0])
		else:
			result.append(right[0])
			right.remove(right[0])

	while left:
		result.append(left[0])
		left.remove(left[0])

	while right:
		result.append(right[0])
		right.remove(right[0])

	return result

# print(merge(random_list(4),random_list(4)))


list = random_list(100)

print(merge_sort(list))
assert merge_sort(list) == sorted(list)



# def merge(left, right):
# 	result = DoubleLinkedList()

# 	if left == None: return right
# 	if right == None: return left

# 	while left.begin and right.begin:
# 		if left.begin.value < right.begin.value:
# 			# print("left_node-added>>", left_node.value)
# 			result.push(left.unshift())
# 		else:
# 			# print("right_node-added>>", right_node.value)
# 			result.push(right.unshift())

# 	# print("post-left>>>", left_node)
# 	# print("post-right>>>", right_node)

# 	# while left.begin:
# 	# 	result.push(left.unshift())	

# 	# while right.begin:
# 	# 	result.push(right.unshift())	

# 	# test = result.begin

# 	# while test:
# 	# 	print(test.value)
# 	# 	test = test.next

# 	return result
