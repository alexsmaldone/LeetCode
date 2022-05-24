class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray = nums[0]

        current_sum = 0
        for n in nums:
            current_sum += n
            max_subarray = max(max_subarray, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_subarray
