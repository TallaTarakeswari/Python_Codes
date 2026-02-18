'''🧠 Correct Two Pointer Thinking

Since array is sorted:

Case 1:

If sum < target
👉 We need bigger sum
👉 Move left pointer forward

Case 2:

If sum > target
👉 We need smaller sum
👉 Move right pointer backward'''



arr = [1, 2, 4, 6, 8, 10]
target = 10

first = 0
last = len(arr) - 1

while first < last:
    current_sum = arr[first] + arr[last]
    
    if current_sum == target:
        print("True")
        break
    elif current_sum > target:
        last -= 1
    else:
        first += 1
else:
    print("False")
