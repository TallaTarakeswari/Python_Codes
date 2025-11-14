'''Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.

Examples:

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: For i = 0, res[i] is 0.
For i = 1, res[i] is 12.
For each position i:

res[i] = product of all elements except arr[i]


Example:

arr = [10, 3, 5, 6, 2]


For index 2 (arr[2] = 5):

res[2] = 10 * 3 * 6 * 2

🧠 KEY TRUTH (The whole reason the method works)

For ANY index i, the all-elements-except-it product can be split into two parts:

( product of all elements BEFORE i )  ×  ( product of all elements AFTER i )


There is nothing else.

That’s the core math.

🎯 EXAMPLE TO SEE THE TRUTH

Take:

arr = [10, 3, 5, 6, 2]
index = 2 (value = 5)


Everything except index 2 is:

10, 3   |   6, 2
 LEFT        RIGHT


So:

res[2] = (10 * 3) × (6 * 2)


Left side is "prefix".
Right side is "suffix".

✔️ Why PREFIX works

We build prefix like this:

prefix[0] = 1               (nothing on the left)
prefix[1] = 10
prefix[2] = 10 * 3 = 30
prefix[3] = 10 * 3 * 5 = 150
prefix[4] = 10 * 3 * 5 * 6 = 900


prefix[i] = product of all elements before i
Exactly what we need.

✔️ Why SUFFIX works

While going reverse:

suffix initially = 1

for i = 4 → suffix = 1
for i = 3 → suffix = 2
for i = 2 → suffix = 6*2 = 12
for i = 1 → suffix = 5*6*2 = 60
for i = 0 → suffix = 3*5*6*2 = 180


suffix = product of all elements after i
Exactly what we need.

🎉 MAGIC HAPPENS HERE

We multiply:

res[i] = prefix[i] × suffix


For index 2:

prefix[2] = 30  (10 * 3)
suffix at index 2 = 12  (6 * 2)

res[2] = 30 * 12 = 360


Is that correct?

YES — because:

10 * 3 * 6 * 2 = 360


So the method is EXACTLY doing:

(LEFT side product) × (RIGHT side product)


Which is the mathematical definition of “all elements except arr[i]”.

🔥 WHY THIS ALWAYS WORKS (Final Logic Proof)

For each index i:

All elements except arr[i]
= arr[0] * arr[1] * ... * arr[i-1]    ×    arr[i+1] * arr[i+2] * ... * arr[n-1]


prefix[i] = product of left part
suffix = product of right part

So:

res[i] = prefix[i] × suffix '''

Code:
=================
class Solution:
    def productExceptSelf(self, arr):
        prefix=1
        suffix=1
        res=[1]* len(arr)
        for i in range(0,len(arr)):
            res[i]=prefix
            prefix *=arr[i]
        for i in range(len(arr)-1,-1,-1):
            res[i] *=suffix
            suffix *=arr[i]
        return(res)


Exact match.
