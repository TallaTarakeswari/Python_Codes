'''You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

 

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.'''

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        k=[]
        for i in range(len(words)):
            if x in words[i]:
                k.append(i)
        return k


class Solution(object):
    def findWordsContaining(self, words, x):
        return [i for i, w in enumerate(words) if x in w]
        
