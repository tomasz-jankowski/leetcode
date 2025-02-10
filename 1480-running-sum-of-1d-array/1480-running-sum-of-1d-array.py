from typing import List


class Solution:
    def runningSum_naive(self, nums: List[int]) -> List[int]:
        """Uses list comprehension and sum(), leading to redundant calculations.

        Time Complexity: O(n²)
        Space Complexity: O(n)
        """
        return [sum(nums[:idx + 1]) for idx, num in enumerate(nums)]

    def runningSum_extra_space(self, nums: List[int]) -> List[int]:
        """Uses an additional list to store results, maintaining immutability.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        ret = []
        _sum = 0
        for num in nums:
            _sum += num
            ret.append(_sum)
        return ret

    def runningSum_in_place(self, nums: List[int]) -> List[int]:
        """Modifies `nums` in place to avoid extra space.

        Time Complexity: O(n)
        Space Complexity: O(1)

        warning: in-place modification
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
