import pdb

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
def shuffle_merge(a,b):
    if not b: return a
    if not a: return b
    
    tail, head, a = a, a, a.next

    while a or b:
        if b:
            tail.next = b
            tail, b = b, b.next
        if a:
            tail.next = a
            tail, a = a, a.next

    return head

def push(head, data):
  n = Node(data)
  n.next = head
  return n

def build_123():
	return push(push(Node(3), 2), 1)
  
def build_456():
	return push(push(Node(6), 5), 4)

listA = build_123()
listB = build_456()

shuffle_merge(listA, listB)