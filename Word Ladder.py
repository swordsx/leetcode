class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        adjacencyList = {}
        wordDict.add(beginWord)
        wordDict.add(endWord)

        queue = [(beginWord, 1)]
        i = 0
        while i < len(queue):
            (curWord, curDepth) = queue[i]
            if curWord == endWord:
                return curDepth
            lenCurWord = len(curWord)
            for j in range(len(curWord)):
                part1 = curWord[:j]
                part2 = curWord[j + 1:]
                for k in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = part1 + k + part2
                    if newWord in wordDict:
                        queue.append((newWord, curDepth + 1))
                        wordDict.remove(newWord)
            i += 1
        return 0Word Ladder
