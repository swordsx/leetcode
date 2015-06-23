class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None

class LRUCache:
    def addNode(self, node):
        node.pre = self.headNode
        node.post = self.headNode.post
        node.pre.post = node
        node.post.pre = node

    def delNode(self, node):
        node.pre.post = node.post
        node.post.pre = node.pre
        del node

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.headNode = ListNode("head", "tail")
        self.headNode.pre = self.headNode
        self.headNode.post = self.headNode
        self.map = {}

    # @return an integer
    def get(self, key):
        if key in self.map:
            self.delNode(self.map[key])
            self.addNode(self.map[key])
            return self.map[key].value
        else: return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map:
            self.delNode(self.map[key])
        node = ListNode(key, value)
        self.addNode(node)
        self.map[key] = node
        if len(self.map) > self.capacity:
            del(self.map[self.headNode.pre.key])
            self.delNode(self.headNode.pre)
