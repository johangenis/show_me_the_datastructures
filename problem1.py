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


def test1():
    print("test 1 init")
    checks = []
    single_value_cache = LRU_Cache(1)
    # value 1 with key 2 is on cache now
    single_value_cache.set(2, 1)

    # check if value is on cache
    checks.append(single_value_cache.get(2) == 1)

    # value should be removed from cache
    single_value_cache.set(3, 4)

    # check if value is on cache
    checks.append(single_value_cache.get(2) == -1)

    # check if value is on cache
    checks.append(single_value_cache.get(3) == 4)

    if all(checks[: sum(checks)]) == True:
        print("Passed")
    else:
        print("Failed")


def test2():
    print("test 2 init")
    checks = []
    cache = LRU_Cache(3)
    # value 1 with key 2 is on cache now
    cache.set(2, 1)

    # check if value is on cache
    checks.append(cache.get(2) == 1)

    # value should be removed from cache
    cache.set(3, 4)

    # check if value is on cache
    checks.append(cache.get(2) == 1)

    # check if value is on cache
    checks.append(cache.get(3) == 4)

    cache.set(4, 6)

    # check if value is on cache
    checks.append(cache.get(2) == 1)

    # check if value is on cache
    checks.append(cache.get(3) == 4)

    # check if value is on cache
    checks.append(cache.get(4) == 6)

    # remove oldest element which should be 2
    cache.set(5, 9)

    # check if value is on cache
    cache.get((2) == -1)

    # check if value is on cache
    checks.append(cache.get(3) == 4)

    # check if value is on cache
    checks.append(cache.get(4) == 6)

    # check if value is on cache
    checks.append(cache.get(5) == 9)

    if all(checks[: sum(checks)]) == True:
        print("Passed")
    else:
        print("Failed")


def test3():
    print("test 3 init")
    checks = []
    single_value_cache = LRU_Cache(2)
    # value 1 with key 2 is on cache now
    single_value_cache.set(2, 1)

    # check if value is on cache
    checks.append(single_value_cache.get(2) == 1)

    # handle collision
    single_value_cache.set(2, 4)

    # 1 value should be overriden
    checks.append(single_value_cache.get(2) == 4)

    single_value_cache.set(3, 1)

    # check if value is on cache
    checks.append(single_value_cache.get(3) == 1)

    # check if value is on cache
    checks.append(single_value_cache.get(2) == 4)

    if all(checks[: sum(checks)]) == True:
        print("Passed")
    else:
        print("Failed")


test1()
test2()
test3()
