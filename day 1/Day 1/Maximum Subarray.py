# 53. Maximum Subarray

# Medium

# Companies:
# Adobe
# Samsung
# Amazon
# Facebook
# Netflix
# Flipkart
# Tekion-corp
# Bloomberg
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi

# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res,s = nums[0],nums[0]
        for i in range(1,len(nums)):
            s = max(nums[i],s+nums[i])
            res = max(s,res)
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1)