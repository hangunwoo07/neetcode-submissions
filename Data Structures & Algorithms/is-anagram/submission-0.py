class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram: Dict[int] = {}

        for char in s:
            if char in anagram:
                anagram[char] += 1
            else:
                anagram[char] = 1
        
        for char in t:
            if char in anagram:
                if anagram[char] > 1:
                    anagram[char] -= 1
                else:
                    anagram.pop(char)
            else:
                return False
        
        if len(anagram) > 0:
            return False
        else:
            return True
            