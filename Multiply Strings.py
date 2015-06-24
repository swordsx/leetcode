class easySolution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))
        
  class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        product = [0] * (len(num1) + len(num2) + 1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                product[i + j] += int(num1[i]) * int(num2[j])
        for i in range(len(product) - 1):
            product[i + 1] += product[i] / 10
            product[i] = str(product[i] % 10)
        while len(product) > 1 and product[-1] == '0' or product[-1] == 0:
            product.pop()
        return ''.join(product[::-1])
