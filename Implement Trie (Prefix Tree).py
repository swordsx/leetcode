class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.dict = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.dict:
                cur.dict[ch] = TrieNode()
            cur = cur.dict[ch]
        cur.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.dict:
                return False
            cur = cur.dict[ch]
        return cur.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.dict:
                return False
            cur = cur.dict[ch]
        return True
