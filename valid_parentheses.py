class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                else:
                    return False
        return True