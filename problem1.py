class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]

    def remove(self, node):
        previous = node.previous
        next = node.next
        previous.next = next
        next.previous = previous

    def add(self, node):
        previous = self.tail.previous
        previous.next = node
        self.tail.previous = node
        node.previous = previous
        node.next = self.tail


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print("Should return 1 and actually returns: {}".format(our_cache.get(1)))  # returns 1
print("Should return 2 and actually returns: {}".format(our_cache.get(2)))  # returns 2
print(
    "Should return -1, because 9 is not present in the cache, and actually returns: {}".format(
        our_cache.get(9)
    )
)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(
    "Should return -1, because the cache reached it's capacity and 3 was the\
 least recently used entry, and actually returns: {}".format(
        our_cache.get(3)
    )
)
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
