class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
#         NON OPTIMAL SOLUTION - O(log n) T | O(n) S for hashset
#         visit = set()
#         while n not in visit:
#             visit.add(n)
#             n = self.sumOfSquares(n)

#             if n == 1:
#                 return True

#         return False

#     def sumOfSquares(self, n):
#         output = 0

#         while n:
#             digit = n % 10
#             digit = digit ** 2
#             output += digit
#             n = n // 10

#         return output

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
