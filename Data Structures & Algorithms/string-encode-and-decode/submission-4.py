class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded: str = ""
        if len(strs) == 0:
            return '\0'
        encoded = "\t".join(word for word in strs)
        return encoded

    def decode(self, s: str) -> list[str]:
        if s == '\0':
            return []

        if len(s) == 0:
            return [""]

        return s.split("\t")
