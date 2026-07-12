class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        new = ''
        for c in s:
            if c.isalnum():
                new += c.lower()

        left, right = 0, len(new) - 1

        while left < right or left == right: 
            
            if new[left] == new[right]:
                left += 1
                right -= 1
            
            else:
                return False

        return True
