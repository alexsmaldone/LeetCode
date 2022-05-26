# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return result
