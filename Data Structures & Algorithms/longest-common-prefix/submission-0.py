class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_range = len(min(strs, key=len))
        pref_list = [str[0:prefix_range] for str in strs]
        while len(set(pref_list)) > 1:
            prefix_range -= 1
            pref_list = [str[0:prefix_range] for str in strs]
        return pref_list[0]