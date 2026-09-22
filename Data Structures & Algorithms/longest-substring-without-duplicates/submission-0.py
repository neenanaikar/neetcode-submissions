class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0

        freq = set()

        for right in range(len(s)):
            

            while s[right] in freq:
                
                freq.remove(s[left])
                left += 1
            freq.add(s[right])
            best = max(best, right - left + 1)
        return best
            

            

