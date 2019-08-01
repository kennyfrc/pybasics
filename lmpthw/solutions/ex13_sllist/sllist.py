import pdb

class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            # nothing net
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end

        assert self.end.next == None

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None and self.begin == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            popped_node = self.end
            node = self.begin
            while node.next != self.end and node.next != None:
                node = node.next
            self.end = node
            self.end.next = None
            return popped_node.value

    def shift(self, obj):
        self.push(obj)

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin == None:
            return None
        elif self.begin == self.end:
            node = self.end
            self.begin = self.end = None
            return node.value
        else:
            unshifted_node = self.begin
            self.begin = self.begin.next
            assert unshifted_node != self.begin
            return unshifted_node.value

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        count = 0
        if self.begin.value == obj:
            self.begin = node.next
            return count
        while node.value != obj:
            node = node.next
            count += 1
        return count

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        node = self.begin
        return node.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        node = self.end
        return node.value

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """Get the value at index."""
        node = self.begin
        count = 0
        while count != index:
            node = node.next
            count += 1
        if node == None:
            return None
        return node.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""