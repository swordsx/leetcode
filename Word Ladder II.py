class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def buildpath(path, depth):
            curWord = path[0]
            if depth == steps:
                if curWord == start:
                    result.append(path)
                return
            for preWord in pre[curWord]:
                buildpath([preWord] + path, depth + 1)
        
        result = []
        dict.add(start)
        dict.add(end)
        pre = collections.defaultdict(list)
        steps = 0x7FFFFFFF
        visited = set()
        length = len(start)
        queue = [(start, 1)]
        while queue:
            curWord, curDepth = queue.pop(0)
            if curDepth == steps: break
            dict.remove(curWord)
            for i in range(length):
                part1 = curWord[:i]
                part2 = curWord[i + 1:]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = part1 + ch + part2
                    if newWord in dict:
                        if newWord == end:
                            steps = curDepth + 1
                        if newWord not in visited:
                            queue.append((newWord, curDepth + 1))
                            visited.add(newWord)
                        pre[newWord].append(curWord)
        buildpath([end], 1)
        return result
