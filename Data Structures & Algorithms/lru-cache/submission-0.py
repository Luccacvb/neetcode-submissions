class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, node: Optional[ListNode]) -> None:
        ref = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = ref
        ref.prev = node

    def _remove(self, node: Optional[ListNode]) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_front(new_node)
