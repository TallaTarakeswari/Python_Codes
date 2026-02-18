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
