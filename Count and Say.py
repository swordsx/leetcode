class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        curStr = '1'
        for i in range(n - 1):
            nextStr = ''; curCh = ''; curCnt = 0
            for ch in curStr:
                if ch == curCh:
                    curCnt += 1
                else:
                    if curCnt != 0:
                        nextStr += str(curCnt) + curCh
                    curCh = ch
                    curCnt = 1
            nextStr += str(curCnt) + curCh
            curStr = nextStr
        return curStr
