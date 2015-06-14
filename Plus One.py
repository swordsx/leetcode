class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carryFlag = 1
        i = len(digits) - 1
        while carryFlag == 1:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
            else:
                digits[i] += 1
                carryFlag = 0
            i -= 1
        return digits
