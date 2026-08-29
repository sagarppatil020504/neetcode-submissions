class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=""
        for char in s[::1]:
            if char.isalnum():
                clean+=char.lower()

        return clean[::1]==clean[::-1]
          

