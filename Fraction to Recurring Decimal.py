class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0: return '0'
        result = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator / denominator)
        numerator %= denominator
        if numerator == 0: return result
        #以上為整數部分
        
        result += '.'
        dict = {}
        head = key = numerator
        n = 0
        while key != 0 and key not in dict:
            if numerator < denominator: numerator *= 10
            dict[key] = {'q' : numerator / denominator}
            numerator %= denominator
            dict[key]['r'] = numerator
            dict[key]['n'] = n
            n += 1
            key = numerator
        #小數部分的計算
            
        m = dict[key]['n'] if key != 0 else n
        key = head
        for i in range(m):
            result += str(dict[key]['q'])
            key = dict[key]['r']
        if key == 0: return result
        #非循環小數輸出
        
        result += '('
        while True:
            result += str(dict[key]['q'])
            key = dict[key]['r']
            if dict[key]['n'] == m: break
        result += ')'
        #循環小數辦輸出
        return result
