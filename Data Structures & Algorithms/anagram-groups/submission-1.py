class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        mp = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            mp[sorted_word].append(word)
        
        return list(mp.values())