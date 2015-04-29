class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        def search(str, nLeft, nRight):
            if nLeft == 0 and nRight == 0:
                list.append(str)
                return
            if nLeft > nRight:            
                return
            if nLeft > 0:
                search(str + '(', nLeft - 1, nRight)
            if nRight > 0:
                search(str + ')', nLeft, nRight - 1)
        list = []
        str = ''
        search(str, n ,n)
        return list
