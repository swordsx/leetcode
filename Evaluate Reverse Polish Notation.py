class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif len(token) > 1 and token[0] == '-':
                stack.append(-int(token[1:]))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+': stack.append(op1 + op2)
                elif token == '-': stack.append(op1 - op2)
                elif token == '*': stack.append(op1 * op2)
                else:
                    if op1 * op2 < 0: stack.append(-(abs(op1) / abs(op2)))
                    else: stack.append(op1 / op2)
        return stack[0]
