'''
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.'''

#Code
#========================
# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        prefix_sum=[0]*(len(arr)+1)

        for i in range(1,len(arr)+1):
            prefix_sum[i]=prefix_sum[i-1]+arr[i-1]
        length=len(prefix_sum)-1
        for i in range(1,len(prefix_sum)):
            if prefix_sum[i-1]==prefix_sum[length]-prefix_sum[i]:
                return(i-1)
        return -1

'''
| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(n)**   |
| Space Complexity | **O(n)**   |

Chat gpt version:
==========================='''

class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            total_sum -= arr[i]  # Now total_sum acts as right_sum

            if left_sum == total_sum:
                return i  # equilibrium point found

            left_sum += arr[i]

        return -1  # no equilibrium found
'''
| Type             | Complexity                            |
| ---------------- | ------------------------------------- |
| Time Complexity  | **O(n)** (two passes: `sum()` + loop) |
| Space Complexity | **O(1)** (no extra array)             |
Optimized Logic (No Prefix Array)

Instead of storing prefix sums, we can:

Compute the total sum of the array.

Traverse the array while maintaining a variable left_sum, and compute right_sum on the fly:

At any index i:

right_sum = total_sum - left_sum - arr[i]


If at any point:

left_sum == right_sum
→ that index is the equilibrium point
'''

