class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        directories = path.split('/')
        stack = []
        for directory in directories:
            if directory == '.' or directory == '': continue
            elif directory == '..':
                if stack: stack.pop()
            else:
                stack.append(directory)
        return '/' + '/'.join(stack)
