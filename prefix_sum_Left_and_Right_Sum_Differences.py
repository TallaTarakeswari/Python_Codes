'''You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
⭐ Compute for each index
i = 0

nums[:0] → [] → left = 0
nums[1:] → [4, 8, 3] → right = 15

difference = |15 - 0| = 15

i = 1

nums[:1] → [10] → left = 10
nums[2:] → [8, 3] → right = 11

difference = |11 - 10| = 1

i = 2

nums[:2] → [10, 4] → left = 14
nums[3:] → [3] → right = 3

difference = |3 - 14| = 11

i = 3

nums[:3] → [10, 4, 8] → left = 22
nums[4:] → [] → right = 0

difference = |0 - 22| = 22

✅ Final Output
[15, 1, 11, 22]'''

#code
=================
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=[0]*len(nums)

        left_sum[0]=0
        final=[0]*len(nums)
        right_sum=[0]*len(nums)
        right_sum[-1]=0

        for i in range(1,len(nums)):
            left_sum[i]=left_sum[i-1]+nums[i-1]


        for i in range(len(nums)-2,-1,-1):
            right_sum[i]=right_sum[i+1]+nums[i+1]
        for i in range(0,len(nums)):
            final[i]=abs(left_sum[i]-right_sum[i])
        return(final)


#using One loop
==============================
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            ans.append(abs(right-left))
        return ans    
    
