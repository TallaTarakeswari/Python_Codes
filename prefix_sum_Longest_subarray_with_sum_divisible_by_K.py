'''Given an array arr[] and a positive integer k, find the length of the longest subarray with the sum of the elements divisible by k.
Note: If there is no subarray with sum divisible by k, then return 0.

Examples :

Input: arr[] = [2, 7, 6, 1, 4, 5], k = 3
Output: 4
Explanation: The subarray [7, 6, 1, 4] has sum = 18, which is divisible by 3.
Input: arr[] = [-2, 2, -5, 12, -11, -1, 7], k = 3
Output: 5
Explanation: The subarray [2, -5, 12, -11, -1] has sum = -3, which is divisible by 3.
Input: arr[] = [1, 2, -2], k = 2
Output: 2
Explanation: The subarray is [2, -2] has sum = 0, which is divisible by 2.
1) The mathematical identity (reminder)

We use prefix sums P[i] = sum(arr[0..i]). For any subarray l..r:

sum(l..r) = P[r] - P[l-1]


We want this sum to be divisible by k:

(P[r] - P[l-1]) % k == 0
⇔ P[r] % k == P[l-1] % k


So two prefix sums having the same remainder (mod k) means the subarray between them has sum divisible by k.

2) How length is computed

If P[r] % k == rem and the earliest index where this remainder appeared is j (i.e. P[j] % k == rem), then the corresponding subarray is from j+1 to r, and its length is:

length = r - (j+1) + 1 = r - j


So when we store seen[rem] = j (earliest j), length is r - seen[rem].

3) The special case when the subarray starts at index 0

If a subarray starts at index 0 and ends at r, then l = 0 and l-1 = -1. The identity above becomes:

sum(0..r) = P[r] - P[-1]


We treat P[-1] as 0. So the condition P[r] % k == P[-1] % k becomes:

P[r] % k == 0


That is, we need remainder 0 to have an imaginary earliest index of -1, because j = l-1 = -1.

So to make the formula length = r - seen[rem] work uniformly for subarrays that start at 0, we must initialize:

seen[0] = -1


This encodes the idea that remainder 0 was seen “before the array starts.”

4) What happens if you do not set seen[0] = -1 (trace A)

Look at the trace labeled WITHOUT seen[0] = -1. Important lines:

At i=2 we get prefix sum 0, rem = 0. Your code stores seen[0] = 2.

That means you now believe the earliest time remainder 0 was seen is index 2.

Later, at i=7, prefix sum again has rem = 0. Your code computes:

length = 7 - seen[0] = 7 - 2 = 5

So you find subarray 3..7 (length 5), because you think remainder 0 first appeared at 2.

But actually the longest subarray divisible by 7 starts at index 0 and ends at 7 (length 8). You missed it because you overwrote the earliest occurrence of rem 0 with 2 instead of having -1.

Final maxi (without init) = 5.

5) What happens if you do set seen[0] = -1 (trace B)

Now we start with seen = {0: -1} meaning the remainder 0 was seen at index -1 (before the array).

At i=2, rem = 0. We see rem is already in seen with value -1.

So length = 2 - (-1) = 3 → subarray 0..2 (length 3) is divisible by 7.

At i=7, rem = 0 again. length = 7 - (-1) = 8 → subarray 0..7 (length 8).

That correctly captures the subarray starting at index 0.
Final maxi (with init) = 8, which is the correct longest length.

6) Intuition summary — why seen[0] = -1 is necessary

The algorithm treats seen[rem] as j = l-1, the index before the start of the subarray whose remainder equals rem.

If a valid subarray starts at the very first element (l = 0), then j = l-1 = -1. To handle that uniformly, we must pre-store seen[0] = -1.

Without it, the first time you encounter remainder 0 you'll store some index i ≥ 0, and that will prevent recognizing longer subarrays that actually start at 0.

7) Quick note about negative numbers and %

In Python, x % k returns a non-negative remainder when k > 0, even if x is negative. So prefix_sum % k is safe for negative prefix sums (no extra normalization needed).
You said:
if 0 reminder at 2 or 3 firsttime then initialzing with at -1 is not correct right
'''

#Code
=================
#User function Template for python3
class Solution:
	def longestSubarrayDivK(self, arr, k):
	    seen={}
	    seen[0]=-1
        prefix_sum=0
        maxi=0

        for i in range(len(arr)):
            prefix_sum+=arr[i]
            rem= prefix_sum%k
            if rem not in seen:
                seen[rem]=i
            else:
                maxi=max(maxi,(i-seen[rem]))
        return maxi
		#Complete the function



Example: -4 % 7 == 3.
