# Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have to
# wait after the ith day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return answer
