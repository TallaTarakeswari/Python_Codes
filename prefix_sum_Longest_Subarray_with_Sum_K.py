'''Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.
Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].'''

Code
===========
class Solution:
    def longestSubarray(self, arr, k):  
        # Initialize the running prefix sum
        prefix_sum = 0

        # Dictionary to store the earliest index where a given prefix_sum occurred
        # Initialize with {0: -1} to handle subarrays starting from index 0
        prefix_map = {0: -1}

        # List to store lengths of subarrays that sum to k (we’ll take max later)
        results = [0]

        # Traverse the array
        for i, num in enumerate(arr):
            # Update prefix sum up to the current index
            prefix_sum += num

            # Case 1: If the entire subarray [0..i] itself sums to k
            if prefix_sum == k:
                results.append(i + 1)  # length = i - 0 + 1 = i + 1

            # Case 2: Check if there exists a previous prefix sum 
            # such that current_sum - previous_sum = k
            # That means subarray (previous_index+1 .. i) sums to k
            if (prefix_sum - k) in prefix_map:
                start = prefix_map[prefix_sum - k] + 1  # start index of subarray
                results.append(i - start + 1)  # length of that subarray

            # Case 3: Store the current prefix_sum with its index
            # Only store if it hasn’t been stored before (keep the earliest occurrence)
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        # Return the maximum length of all found subarrays
        return max(results)
