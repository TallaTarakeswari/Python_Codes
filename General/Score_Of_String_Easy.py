class Solution(object):
    def scoreOfString(self, s):
        t_sum=0
        for i in range(0,len(s)-1,1):
            t_sum += abs(ord(s[i])-ord(s[i+1]))
        print(t_sum)
            
        
a=Solution()
a.scoreOfString("")
