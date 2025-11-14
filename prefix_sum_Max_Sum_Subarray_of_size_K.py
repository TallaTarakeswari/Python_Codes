'''Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.
Edge cases & notes

If k <= 0 → invalid (raise error).

If k > n → no windows (return []).

Be careful about inclusive indices: a window starting at i with length k ends at r = i + k - 1.

For many repeated queries of arbitrary (l, r) on the same array, prefix sums are excellent because each query is O(1). For a single-pass fixed k, sliding-window is slightly simpler and uses less memory.'''

#Code:
===============

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        maximum=0
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1,len(arr)):
            prefix[i] +=prefix[i-1]+arr[i]
        for i in range(0,len(arr)-k+1):
            if i==0:
                prefix_sum=prefix[i+k-1]
                maximum=max(maximum,prefix_sum)
            else:
                prefix_sum=prefix[i+k-1]-prefix[i-1]
                maximum=max(maximum,prefix_sum)
        return(maximum)
