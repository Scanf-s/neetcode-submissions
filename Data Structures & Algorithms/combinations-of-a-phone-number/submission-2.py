class Solution:

    def recursion(self, matcher: dict[str, list[str]], number: str, idx: int, cur: list[str], candidates: list[str]) -> None:
        if len(cur) == len(number):
            candidate: str = ''.join(ch for ch in cur)
            candidates.append(candidate)
            return
        
        characters: list[str] = matcher[number[idx]]
        for char in characters:
            cur.append(char)
            self.recursion(matcher, number, idx + 1, cur, candidates)
            cur.pop()
            

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        matcher: dict[str, list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ans: list[str] = []
        self.recursion(matcher, digits, 0, [], ans)
        return ans
