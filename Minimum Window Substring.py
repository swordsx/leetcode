class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        result = s
        targetmap = {}
        curmap = {}
        for ch in t:
            if ch not in targetmap: targetmap[ch] = 1
            else: targetmap[ch] += 1
            curmap[ch] = 0
        slow = 0; fast = 0
        while fast < len(s):
            if s[fast] in curmap:
                curmap[s[fast]] += 1
            fast += 1
            finish = True
            for ch in targetmap:
                if curmap[ch] < targetmap[ch]:
                    finish = False
            if fast == len(s) and not finish:
                return ''
            if finish:
                break
        while s[slow] not in targetmap or curmap[s[slow]] > targetmap[s[slow]]:
            if s[slow] in targetmap and curmap[s[slow]] > targetmap[s[slow]]:
                curmap[s[slow]] -= 1
            slow += 1
        result = s[slow:fast]

        curCH = s[slow]
        while fast < len(s):
            curCH = s[slow]
            while slow < len(s) and (s[slow] not in curmap or (s[slow] == curCH and curmap[curCH] >= targetmap[curCH])):
                if curCH == s[slow]:
                    curmap[curCH] -= 1
                slow += 1
                if curmap[curCH] >= targetmap[curCH] and fast - slow < len(result):
                    result = s[slow:fast]
            while curmap[curCH] < targetmap[curCH] and fast < len(s):
                if s[fast] in curmap:
                    curmap[s[fast]] += 1
                fast += 1
            if curmap[curCH] >= targetmap[curCH] and fast - slow < len(result) and slow < len(s):
                result = s[slow:fast]

        if slow < len(s) and curmap[curCH] >= targetmap[curCH]:
            while s[slow] not in targetmap or curmap[s[slow]] > targetmap[s[slow]]:
                if s[slow] in targetmap and curmap[s[slow]] > targetmap[s[slow]]:
                    curmap[s[slow]] -= 1
                slow += 1
            if fast - slow < len(result) and slow < len(s):
                result = s[slow:fast]
            
        return result
