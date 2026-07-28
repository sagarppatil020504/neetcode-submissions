class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen =list(s)
        if len(s) != len(t):
            return False
        for letter in list(t):
            if letter in seen:
                seen.remove(letter)
        if len(seen) == 0:
            return True 
        else:
            return False    


