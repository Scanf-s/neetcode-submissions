class Solution:

    def recursion(self, matcher: dict[int, list[str]], number: str, cur: list[str], candidates: list[str]) -> None:
        if not number:
            candidate: str = ''.join(ch for ch in cur)
            candidates.append(candidate)
            return
        
        characters: list[str] = matcher[int(number[0])]
        for char in characters:
            cur.append(char)
            self.recursion(matcher, number[1:], cur, candidates)
            cur.pop()
            

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        matcher: dict[int, list[str]] = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        ans: list[str] = []
        self.recursion(matcher, digits, [], ans)
        return ans
