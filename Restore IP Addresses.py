class Solution:
    # @param {string} s
    # @return {string[]}
    def search(self, s, n, IPs):
        if s == '' or n == 4:
            if s == '' and n == 4:
                self.result.append('.'.join(IPs))
        elif s[0] == '0':
            self.search(s[1:], n + 1, IPs + ['0'])
        else:
            for i in range(1, min(4, len(s) + 1)):
                if int(s[:i]) <= 255:
                    self.search(s[i:], n + 1, IPs + [s[:i]])
        
    def restoreIpAddresses(self, s):
        self.result = []
        self.search(s, 0, [])
        return self.result
