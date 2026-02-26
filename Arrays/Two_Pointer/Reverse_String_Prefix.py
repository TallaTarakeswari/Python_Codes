'''You are given a string s and an integer k.

Reverse the first k characters of s and return the resulting string.

 

Example 1:

Input: s = "abcd", k = 2

Output: "bacd"

Explanation:​​​​​​​

The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".

Example 2:

Input: s = "xyz", k = 3

Output: "zyx"

Explanation:

The first k = 3 characters "xyz" are reversed to "zyx". The final resulting string is "zyx".

Example 3:

Input: s = "hey", k = 1

Output: "hey"

Explanation:

The first k = 1 character "h" remains unchanged on reversal. The final resulting string is "hey".

 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
1 <= k <= s.length'''

'''my approch
✔ Time Complexity = O(k)

✔ Space Complexity = O(n) (because of list conversion)'''

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        right= k-1
        left=0
        li=list(s)
        while(right>left):
            li[right],li[left]=li[left],li[right]
            right -=1 
            left +=1 
            s="".join(li)
        return(s)


#simple approch
s = "xyz"
k=3
s=s[:k][::-1]+s[k:]
print(s)

        
