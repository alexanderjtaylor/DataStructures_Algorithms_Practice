

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left starts at beginning of s and right starts at the end         
        left, right = 0, len(s) - 1
        # While left is before right        
        while left < right:
            # If left is not an alpha-numeric character then advance left            
            if not s[left].isalnum():
                left += 1
            # If right is not an alpha-numeric character then advance(move left) right
            elif not s[right].isalnum():
                right -= 1
            # Both left and right are alpha-numeric characters at this point so if they do not match return the fact that input was non-palendromic
            elif s[left].lower() != s[right].lower():
                return False
            # Otherwise characters matched and we should look at the next pair of characters
            else:
                left, right = left + 1, right - 1
        # The entire stirng was verified and we return the fact that the input string was palendromic         
        return True