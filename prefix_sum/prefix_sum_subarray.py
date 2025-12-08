'''Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.'''

#User function Template for python3
class Solution:
    def subarraySum(self,arr, target):
        prefix_sum=0
        prefix_map={}
        for i ,num in enumerate(arr):
            prefix_sum +=num
        #array starts with index 0
            if prefix_sum==target:
                return[1,i+1]
        #adding prefixes to the dictornary
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum]=i
        #if subarray starts somewhere in the array
            if prefix_sum-target in prefix_map:
                start_index=prefix_map[prefix_sum-target]+1
            #making 0 based index
                return [start_index+1,i+1]
        return [-1]
