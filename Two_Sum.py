'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

code: O(n^2)
=============
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums=0;m=0;i=1
        while(i<=len(nums)-1):
            sums += nums[m]+nums[i]
            if sums== target:
                return[m,i]
            else:
                sums=0
                i=i+1
            if i>len(nums)-1:
                m=m+1
                i=m+1

code: O(n) using hashmap dictonary
======================================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],i]
            seen[diff]=i
        
