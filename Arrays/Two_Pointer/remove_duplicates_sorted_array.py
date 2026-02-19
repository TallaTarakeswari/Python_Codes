'''
🧠 Core Idea

Since the array is sorted, duplicates will always be next to each other.

So instead of checking the whole array, we only compare:

arr[scan]  with  arr[scan - 1]


If they are different → we found a new unique element.

🎯 What Each Variable Does
✅ scan

Moves forward one by one

Checks every element

Think of it as the reader pointer

✅ write

Points to where the next unique element should be placed

Think of it as the writer pointer

🔍 Step-by-Step Execution

Initial:

arr = [1,1,2,2,3,3,3,4]
write = 1


We start loop from index 1.

Iteration 1 → scan = 1

Compare:

arr[1] = 1
arr[0] = 1


They are equal ❌
So skip.

write = 1

Iteration 2 → scan = 2

Compare:

arr[2] = 2
arr[1] = 1


Different ✅
So:

arr[write] = arr[2]
arr[1] = 2


Now array becomes:

[1,2,2,2,3,3,3,4]


Increment:

write = 2

Iteration 3 → scan = 3

Compare:

arr[3] = 2
arr[2] = 2


Same ❌
Skip.

Iteration 4 → scan = 4

Compare:

arr[4] = 3
arr[3] = 2


Different ✅

arr[write] = arr[4]
arr[2] = 3


Array becomes:

[1,2,3,2,3,3,3,4]


Increment:

write = 3

Iteration 5 → scan = 5

Compare:

arr[5] = 3
arr[4] = 3


Same ❌

Iteration 6 → scan = 6

Compare:

arr[6] = 3
arr[5] = 3


Same ❌

Iteration 7 → scan = 7

Compare:

arr[7] = 4
arr[6] = 3


Different ✅

arr[write] = arr[7]
arr[3] = 4


Array becomes:

[1,2,3,4,3,3,3,4]


Increment:

write = 4

🏁 Final Output

We print:

print(arr[:write])


write = 4

So output is:

[1, 2, 3, 4]

💡 Why We Use arr[:write]

Because only first write elements are unique.

The rest of array may contain leftover values, but we ignore them.

🧮 Time and Space Complexity
⏱ Time Complexity:
O(n)


We scan array once.

📦 Space Complexity:
O(1)


No extra space used (in-place).

🎯 Why This Works Only For Sorted Array

Because duplicates are adjacent.

If array was:

[1,2,1,3]


This logic would fail.'''

arr = [1,1,2,2,3,3,3,4]
write=1 
for scan in range(1,len(arr)):
  if arr[scan]!=arr[scan-1]:
    arr[write]=arr[scan]
    write +=1 
print(arr[:write])
