class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.trie = {}
        

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['#'] = {}           
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self._search(word, self.trie)

    def _search(self, word, cur):
        if word == '' :
            return '#' in cur
        ch = word[0]
        if ch != '.':
            if ch not in cur:
                return False
            else: return self._search(word[1:], cur[ch])
        else:
            result = False
            for key in cur:
                result |= self._search(word[1:], cur[key])
                if result: return result
            return result
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
