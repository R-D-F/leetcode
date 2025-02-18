# Given a sorted array of distinct integers and a target value, return the index
# if the target is found. If not, return the index where it would be if it were inserted in order.


# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for count, i in enumerate(nums):
            if i == target:
                return count
            elif i > target:
                return count
            elif count + 1 == len(nums):
                return count + 1


NUMS = [1, 3, 5, 6]
TARGET = 5

sol = Solution()

print(f"Example 1:\n{sol.searchInsert(NUMS, TARGET)}")
