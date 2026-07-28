class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq = [0]*26
        if len(s) != len(t):
            return False
        for i in range (min(len(s),len(t))):
            freq[ord(s[i])-ord("a")]+=1
            freq[ord(t[i])-ord("a")]-=1

        if all (x==0 for x in freq)>0:
            return True
        else:
            return False