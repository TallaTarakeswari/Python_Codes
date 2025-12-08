def subarraySum(arr, target):
    prefix_sum = 0
    prefix_map = {0: -1}  # Handle subarrays starting from index 0
    results = []

    for i, num in enumerate(arr):
        prefix_sum += num

        # If a subarray (from start) sums to target
        if prefix_sum == target:
            results.append((0, i))

        # If there's a previous prefix_sum such that the subarray between them = target
        if (prefix_sum - target) in prefix_map:
            start = prefix_map[prefix_sum - target] + 1
            results.append((start, i))

        # Store current prefix_sum if not already stored
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    # Print subarrays and return results
    for (l, r) in results:
        print(arr[l:r+1], "=> indices:", [l, r])
    return results


# Example
arr = [1, 2, 3, 7, 5]
target = 12
print("Results:", subarraySum(arr, target))
