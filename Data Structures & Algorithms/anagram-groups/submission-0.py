class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = {}

        for i in strs:
            sorted_key = "".join(sorted(i))
            
            # Check if the sorted string is not yet a key in our dictionary
            if sorted_key not in anagram_map:
                anagram_map[sorted_key] = list()
            
            anagram_map[sorted_key].append(i)

        # Return only the grouped values as a list of lists
        return list(anagram_map.values())