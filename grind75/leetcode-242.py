

class Solution():
    def isAnagram(self, s, t):
        # In case of different length of two strings return false
        if len(s) != len(t):
            return False
        for idx in set(s):
            # Compare s and t for every index from 0 to 26
            # If they are different, return false
            if s.count(idx) != t.count(idx):
                return False
            # Otherwise, return true
        return True