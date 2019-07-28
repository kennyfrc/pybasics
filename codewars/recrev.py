class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def push(head, data):
  n = Node(data)
  n.next = head
  return n

def reverse(head, tail=None):
	if head:
		return reverse(head.next, Node(head.data, tail))
	else:
		return tail

def build_123():
	return push(push(Node(3), 2), 1)

listA = build_123()
listB = reverse(listA)