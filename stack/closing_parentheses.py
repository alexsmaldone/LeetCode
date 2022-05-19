class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closingBrackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if bracket not in closingBrackets:
                stack.append(bracket)
                continue
            if not stack or stack[-1] != closingBrackets[bracket]:
                return False
            stack.pop()

        return not stack
