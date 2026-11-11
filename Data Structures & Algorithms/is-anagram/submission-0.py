from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict: dict[str, int] = Counter(s)
        t_dict: dict[str, int] = Counter(t)

        if len(s_dict) != len(t_dict):
            return False
        
        for key in s_dict.keys():
            if s_dict[key] != t_dict[key]:
                return False
        return True
