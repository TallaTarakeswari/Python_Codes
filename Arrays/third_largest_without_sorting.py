'''
Very Important Concept (Interview Favorite)

Whenever new largest appears:

second = old largest
largest = new value


Because the previous largest automatically becomes second largest.

Shortcut Memory Trick

Think like this:

“Whenever king changes, old king becomes vice-king.”
Why we need elif

Look at this part:

if x > largest:
    second = largest
    largest = x
elif x > second and x != largest:
    second = x


Two possibilities when reading a new number x:

Case 1 — New number becomes largest

Then we must update:

largest
second


This is handled by:

if x > largest:

Case 2 — Number is not largest, but bigger than second

Then it should become second largest.

That is why:

elif x > second

Example to understand

Suppose:

largest = 10
second  = 6


Now new number:

x = 8


Check:

8 > 10 → False


But:

8 > 6 → True


So 8 should become second largest.

'''
arr = [3,5,2,4,9,62,63]

largest = second = -1

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print(second)
