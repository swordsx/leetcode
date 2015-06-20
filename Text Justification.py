class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        result = []
        begin = 0
        while begin < len(words):
            curWidth = len(words[begin])
            end = begin + 1
            while curWidth < maxWidth:
                print begin, end, curWidth
                if end == len(words) or curWidth + 1 + len(words[end]) > maxWidth:
                    break
                else:
                    curWidth += 1 + len(words[end])
                    end += 1
            extraSpaces = maxWidth - curWidth
            curStr = words[begin]
            print curStr
            if end == len(words) or end == begin + 1:
                for i in range(begin + 1, end):
                    curStr += ' ' + words[i]
                curStr += ' ' * (maxWidth - len(curStr))
                print curStr
            else:
                for i in range(begin + 1, end):
                    print begin, end, extraSpaces
                    curStr += ' ' * (extraSpaces / (end - begin - 1) + 1)
                    if i - begin <= (extraSpaces % (end - begin - 1)):
                        curStr += ' '
                    curStr += words[i]
                    print curStr
            begin = end
            result.append(curStr)
        return result
