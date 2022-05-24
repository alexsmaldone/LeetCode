# You are given a large integer represented as an integer array digits, where
# each digits[i] is the ith digit of the integer. The digits are ordered from
#  most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)

        for i in range(n):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits
