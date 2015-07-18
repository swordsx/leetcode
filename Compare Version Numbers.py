class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1Subs, v2Subs = version1.split('.'), version2.split('.')
        len1, len2 = len(v1Subs), len(v2Subs)
        for i in range(len1):
            v1Subs[i] = int(v1Subs[i]) if v1Subs[i] else 0
        for i in range(len2):
            v2Subs[i] = int(v2Subs[i]) if v2Subs[i] else 0
        for i in range(max(len1, len2)):
            v1Sub = 0 if i >= len1 else v1Subs[i]
            v2Sub = 0 if i >= len2 else v2Subs[i]
            if v1Sub < v2Sub: return -1
            elif v1Sub > v2Sub: return 1
        return 0
