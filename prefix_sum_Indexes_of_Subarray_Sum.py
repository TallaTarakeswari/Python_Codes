'''Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.'''

#Code
#=====================
#my version
#============================
#User function Template for python3
class Solution:
    def subarraySum(self,arr, target):
        prefix=[0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            prefix[i]=prefix[i-1]+arr[i-1]

        seen={}
        for j in range(0,len(prefix)):
            if prefix[j] not in seen:
                seen[prefix[j]]=j
        for k in range(0,len(prefix)):
            start=prefix[k]-target
            if start in seen:
                return [seen[start]+1,k]
        return [-1]

#chatgpt version
#===============================
class Solution:
    def subarraySum(self, arr, target):
        prefix_sum = 0
        seen = {0: 0}   # prefix sum before the array starts
                        # means prefix_sum = 0 at index 0

        for i in range(1, len(arr) + 1):
            prefix_sum += arr[i - 1]

            # check if (prefix_sum - target) already seen
            need = prefix_sum - target
            if need in seen:
                return [seen[need] + 1, i]

            # store prefix sum if not seen
            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return [-1]
